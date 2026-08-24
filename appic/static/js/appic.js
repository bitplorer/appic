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

  function postAction(action, args, originEl) {
    var surface = action.split(".")[0];
    var target =
      document.getElementById(surface) ||
      (originEl && originEl.closest("form, section, aside, div")) ||
      document.getElementById("main");
    var body = new URLSearchParams(args || {});
    fetch("/action/" + action, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "HX-Request": "true",
        "X-Appic-Morph": "1",
      },
      body: body,
    })
      .then(function (r) {
        var bag = r.headers.get("X-Appic-Bag");
        if (bag != null) updateBag(bag);
        var headerSurface = r.headers.get("X-Appic-Surface");
        if (headerSurface) surface = headerSurface;
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
        var node = document.getElementById(surface) || target;
        morph(node, html);
      })
      .catch(function () {});
  }

  document.addEventListener("click", function (ev) {
    var t = closestAction(ev.target);
    if (!t) return;
    if (t.tagName === "A") return;
    var action = t.getAttribute("data-ux-action");
    if (!action) return;
    if (t.tagName === "BUTTON" && t.type === "submit") return;
    ev.preventDefault();
    postAction(action, argsFrom(t), t);
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

  document.addEventListener("keydown", function (ev) {
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
        paths: ["/", "/atelier", "/commission", "/bag", "/board", "/studio", "/lab", "/trace", "/ledger"],
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
