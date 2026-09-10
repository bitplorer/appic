(function () {
  var CHANNEL = "grok-preview-bridge";
  if (window.parent === window) return;
  function safe(path) {
    if (!path || path.charAt(0) !== "/" || path.indexOf("//") === 0) return false;
    try {
      return new URL(path, "https://preview.invalid").origin === "https://preview.invalid";
    } catch (e) {
      return false;
    }
  }
  function go(path) {
    if (!safe(path)) return;
    window.location.assign(path);
  }
  window.addEventListener("message", function (ev) {
    var data = ev && ev.data;
    if (!data || data.channel !== CHANNEL || data.version !== 1) return;
    if (data.type === "navigate" && typeof data.path === "string") go(data.path);
    if (data.type === "history" && (data.delta === -1 || data.delta === 1)) window.history.go(data.delta);
    if (data.type === "hello") {
      try {
        ev.source && ev.source.postMessage(
          { channel: CHANNEL, version: 1, type: "ready", paths: [] },
          ev.origin
        );
      } catch (e) {}
    }
  });
})();
