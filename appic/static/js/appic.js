/* APPIC control plane: data-ux-action → morph. Preview bridge. Command. */
(function () {
  var CHANNEL = "grok-preview-bridge";
  var VERSION = 1;

  function closestAction(el) {
    while (el && el !== document) {
      if (el.getAttribute && el.getAttribute("data-ux-action")) return el;
      el = el.parentElement;
    }
    return null;
  }

  function argsFrom(el) {
    var args = {};
    if (!el || !el.attributes) return args;
    Array.prototype.forEach.call(el.attributes, function (attr) {
      if (attr.name.indexOf("data-ux-arg-") === 0) {
        args[attr.name.slice(12)] = attr.value;
      }
    });
    return args;
  }

  function morph(target, html) {
    if (!target) return;
    if (window.Idiomorph) {
      window.Idiomorph.morph(target, html, { morphStyle: "outerHTML" });
    } else {
      target.outerHTML = html;
    }
  }

  function updateBag(count) {
    document.querySelectorAll("[data-bag-count]").forEach(function (n) {
      n.textContent = String(count);
    });
  }

  function showSeal() {
    var el = document.getElementById("seal-burst");
    if (!el) return;
    el.hidden = false;
    window.setTimeout(function () {
      el.hidden = true;
    }, 720);
  }

  function pushRibbon(kind, verb) {
    var list = document.querySelector(".ribbon-list");
    if (!list) return;
    var li = document.createElement("li");
    li.className = "ribbon-op";
    li.innerHTML =
      '<span class="ribbon-kind"></span><span class="mono"></span>';
    li.querySelector(".ribbon-kind").textContent = kind || "morph";
    li.querySelector(".mono").textContent = verb || "";
    list.insertBefore(li, list.firstChild);
    while (list.children.length > 5) list.removeChild(list.lastChild);
  }

  var inflight = {};

  function postAction(action, args, originEl) {
    var surface = action.split(".")[0];
    var slotSel =
      (originEl && originEl.getAttribute && originEl.getAttribute("data-channel-target")) ||
      "";
    var target =
      (slotSel && document.querySelector(slotSel)) ||
      document.getElementById(surface) ||
      (originEl && originEl.closest("form, section, aside, div")) ||
      document.getElementById("main");
    var body = new URLSearchParams(args || {});
    if (inflight[action]) {
      try {
        inflight[action].abort();
      } catch (e) {}
    }
    var ac = new AbortController();
    inflight[action] = ac;
    fetch("/action/" + action, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "HX-Request": "true",
        "X-Appic-Morph": "1",
      },
      body: body,
      signal: ac.signal,
    })
      .then(function (r) {
        var bag = r.headers.get("X-Appic-Bag");
        if (bag != null) updateBag(bag);
        var headerSurface = r.headers.get("X-Appic-Surface");
        if (headerSurface) surface = headerSurface;
        var headerTarget = r.headers.get("X-Appic-Target");
        if (headerTarget) slotSel = headerTarget;
        var kind = r.headers.get("X-Appic-Kind");
        if (kind === "cap") showSeal();
        var op = r.headers.get("X-Appic-Op");
        if (op) pushRibbon(kind || "morph", op);
        return r.text();
      })
      .then(function (html) {
        if (action.indexOf("palette.") === 0 && surface !== "palette") {
          var pal = document.getElementById("palette");
          if (pal) {
            pal.setAttribute("hidden", "");
            pal.setAttribute("data-open", "0");
          }
        }
        var node =
          (slotSel && document.querySelector(slotSel)) ||
          document.getElementById(surface) ||
          target;
        morph(node, html);
      })
      .catch(function (err) {
        if (err && err.name === "AbortError") return;
      });
  }

  document.addEventListener("click", function (ev) {
    var t = closestAction(ev.target);
    if (!t) return;
    if (t.tagName === "A") return;
    var action = t.getAttribute("data-ux-action");
    if (!action) return;
    if (t.tagName === "BUTTON" && t.type === "submit") return;
    ev.preventDefault();
    var args = argsFrom(t);
    var form = t.closest && t.closest("form");
    if (form) {
      new FormData(form).forEach(function (v, k) {
        if (args[k] == null || args[k] === "") args[k] = v;
      });
    }
    postAction(action, args, t);
  });

  document.addEventListener("submit", function (ev) {
    var form = ev.target;
    if (!form || !form.getAttribute) return;
    if (!(form.getAttribute("data-ux") || form.querySelector("[data-ux-action]"))) return;
    var btn = form.querySelector("[data-ux-action]");
    var action =
      (btn && btn.getAttribute("data-ux-action")) ||
      (form.getAttribute("action") || "").replace(/^\/action\//, "");
    if (!action) return;
    ev.preventDefault();
    var data = {};
    new FormData(form).forEach(function (v, k) {
      data[k] = v;
    });
    Object.assign(data, argsFrom(btn || form));
    postAction(action, data, form);
  });

  /* Wave 1 Signal: data-channel-on synthesizers. Product never imports ux_channel. */
  function channelOn(el) {
    return (el && el.getAttribute && (el.getAttribute("data-channel-on") || "")) || "";
  }

  function fireChannel(el) {
    var action = el.getAttribute("data-ux-action") || el.getAttribute("data-channel-action");
    if (!action) return;
    var args = argsFrom(el);
    if (el.tagName === "INPUT" || el.tagName === "TEXTAREA") {
      args[el.getAttribute("name") || "q"] = el.value;
      args.value = el.value;
    }
    postAction(action, args, el);
  }

  var inputTimers = new WeakMap();
  document.addEventListener("input", function (ev) {
    var el = ev.target;
    if (!el || !el.getAttribute) return;
    var spec = channelOn(el);
    if (spec.indexOf("input delay:") !== 0) return;
    var ms = parseInt(spec.split(":")[1], 10) || 300;
    var prev = inputTimers.get(el);
    if (prev) window.clearTimeout(prev);
    inputTimers.set(
      el,
      window.setTimeout(function () {
        fireChannel(el);
      }, ms)
    );
  });

  function parseSwipe(spec) {
    var parts = (spec || "").split(/\s+/).filter(Boolean);
    return {
      click: parts.indexOf("click") >= 0,
      vertical: parts.indexOf("swipe.vertical") >= 0,
      horizontal: parts.indexOf("swipe.horizontal") >= 0,
      down: parts.indexOf("swipe.down") >= 0,
      right: parts.indexOf("swipe.right") >= 0,
      left: parts.indexOf("swipe.left") >= 0,
      longpress: parts.indexOf("longpress") >= 0,
    };
  }

  var swipe = { el: null, x: 0, y: 0, t: 0, timer: null };
  function pointerEl(ev) {
    var n = ev.target;
    while (n && n !== document) {
      if (n.getAttribute && channelOn(n)) return n;
      n = n.parentElement;
    }
    return null;
  }
  document.addEventListener("pointerdown", function (ev) {
    var el = pointerEl(ev);
    if (!el) return;
    var spec = parseSwipe(channelOn(el));
    swipe.el = el;
    swipe.x = ev.clientX;
    swipe.y = ev.clientY;
    swipe.t = Date.now();
    if (spec.longpress) {
      swipe.timer = window.setTimeout(function () {
        fireChannel(el);
        swipe.el = null;
      }, 480);
    }
  });
  document.addEventListener("pointermove", function (ev) {
    if (!swipe.el) return;
    var dx = ev.clientX - swipe.x;
    var dy = ev.clientY - swipe.y;
    if (Math.abs(dx) + Math.abs(dy) > 8 && swipe.timer) {
      window.clearTimeout(swipe.timer);
      swipe.timer = null;
    }
  });
  document.addEventListener("pointerup", function (ev) {
    if (swipe.timer) {
      window.clearTimeout(swipe.timer);
      swipe.timer = null;
    }
    var el = swipe.el;
    swipe.el = null;
    if (!el) return;
    var spec = parseSwipe(channelOn(el));
    var dx = ev.clientX - swipe.x;
    var dy = ev.clientY - swipe.y;
    var ax = Math.abs(dx);
    var ay = Math.abs(dy);
    var fired = false;
    if (ay > 36 && ay > ax * 1.2) {
      if (spec.vertical || (spec.down && dy > 0)) {
        fireChannel(el);
        fired = true;
      }
    } else if (ax > 36 && ax > ay * 1.2) {
      if (spec.horizontal || (spec.right && dx > 0) || (spec.left && dx < 0)) {
        fireChannel(el);
        fired = true;
      }
    }
    if (!fired && spec.click && Date.now() - swipe.t < 400) {
      /* click already handled by click listener for data-ux-action */
    }
  });
  document.addEventListener("pointercancel", function () {
    if (swipe.timer) window.clearTimeout(swipe.timer);
    swipe.el = null;
    swipe.timer = null;
  });

  window.addEventListener("keydown", function (ev) {
    var meta = ev.metaKey || ev.ctrlKey;
    if (meta && (ev.key === "k" || ev.key === "K")) {
      ev.preventDefault();
      postAction("palette.toggle", {});
      return;
    }
    if (ev.key === "Escape") {
      var pal = document.getElementById("palette");
      if (pal && pal.getAttribute("data-open") === "1") {
        postAction("palette.close", {});
      }
    }
  });

  window.addEventListener("offline", function () {
    document.body.classList.add("is-offline");
  });
  window.addEventListener("online", function () {
    document.body.classList.remove("is-offline");
  });

  function installBridge() {
    if (window.parent === window) return;
    var ancestor =
      location.ancestorOrigins && location.ancestorOrigins.length
        ? location.ancestorOrigins[0]
        : null;
    var parentOrigin = null;
    try {
      if (document.referrer) parentOrigin = new URL(document.referrer).origin;
    } catch (e) {}
    if (ancestor) parentOrigin = ancestor;
    if (!parentOrigin) return;

    function post(msg) {
      window.parent.postMessage(msg, parentOrigin);
    }
    function report() {
      post({
        channel: CHANNEL,
        version: VERSION,
        type: "location",
        path: location.pathname || "/",
        search: location.search,
        hash: location.hash,
      });
      post({
        channel: CHANNEL,
        version: VERSION,
        type: "routes",
        paths: ["/", "/enter", "/desk", "/house", "/visit", "/signal", "/atelier", "/commission", "/bag", "/board", "/studio", "/lab", "/lattice", "/trace", "/ledger", "/clocks", "/health", "/pulse"],
      });
      post({ channel: CHANNEL, version: VERSION, type: "ready" });
    }
    window.addEventListener("message", function (event) {
      if (event.source !== window.parent) return;
      var d = event.data;
      if (!d || d.channel !== CHANNEL || d.version !== VERSION) return;
      if (d.type === "hello") report();
      if (d.type === "navigate" && d.path && d.path.charAt(0) === "/") {
        location.assign(d.path);
      }
      if (d.type === "history" && typeof d.delta === "number") {
        if (!(d.delta === -1 && history.length <= 1)) history.go(d.delta);
      }
    });
    report();
  }
  installBridge();
})();
