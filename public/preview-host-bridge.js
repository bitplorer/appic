/* Guest side of the grok-web ↔ sandbox preview postMessage bridge. */
(function () {
  var CHANNEL = "grok-preview-bridge";
  var VERSION = 1;
  if (typeof window === "undefined" || window.parent === window) return;

  function isSafe(path) {
    if (!path || path.charAt(0) !== "/" || path.indexOf("//") === 0 || path.indexOf("\\") >= 0) return false;
    try {
      var u = new URL(path, "https://preview.invalid");
      return u.origin === "https://preview.invalid";
    } catch (e) {
      return false;
    }
  }

  function routes() {
    return [
      "/", "/enter", "/house", "/commission", "/market", "/forge", "/rail",
      "/studio", "/overlay", "/trace", "/docs", "/deploy", "/login", "/otp",
      "/hello", "/health", "/pulse", "/clocks", "/notes", "/author", "/copy"
    ];
  }

  window.addEventListener("message", function (ev) {
    var data = ev.data;
    if (!data || data.channel !== CHANNEL) return;
    if (data.type === "hello") {
      ev.source.postMessage({
        channel: CHANNEL,
        version: VERSION,
        type: "hello-ok",
        routes: routes()
      }, ev.origin);
    } else if (data.type === "navigate" && isSafe(data.path)) {
      window.location.assign(data.path);
    } else if (data.type === "history" && (data.delta === -1 || data.delta === 1)) {
      window.history.go(data.delta);
    }
  });
})();
