# Interactive WASM Pyodide Playground

Run **`brando.`** brand availability discovery directly in your browser powered by WebAssembly.

---

<div id="pyodide-loading" style="padding: 16px; background: #0F172A; color: #FFFFFF; border-radius: 8px; font-weight: bold;">
  ⚡ Loading Pyodide WebAssembly runtime environment...
</div>

<div id="playground-container" style="margin-top: 20px;">
  <textarea id="python-code" rows="8" style="width: 100%; font-family: monospace; padding: 12px; border-radius: 8px; border: 1px solid #CBD5E1; background: #F8FAFC;">
import brando

# Generate brand candidates programmatically
pipeline = brando.Pipeline()
candidates = pipeline.generate(keywords=["cyber", "nexus"], count=5)

for c in candidates:
    print(f"Name: {c.name:<12} Euphony: {c.euphony_score:.2f}")
  </textarea>
  <br/>
  <button id="run-btn" style="margin-top: 10px; padding: 10px 20px; background: #2563EB; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">
    ▶ Run Python Code in WASM
  </button>
  <pre style="margin-top: 15px; padding: 16px; background: #090D16; color: #F8FAFC; border-radius: 8px;"><code id="output">Output will appear here upon execution...</code></pre>
</div>

<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<script>
  async function main() {
    try {
      let pyodide = await loadPyodide();
      document.getElementById('pyodide-loading').style.display = 'none';
      document.getElementById('output').innerText = 'Pyodide WASM Runtime Loaded Successfully!';
      
      document.getElementById('run-btn').addEventListener('click', async () => {
        let code = document.getElementById('python-code').value;
        try {
          let result = await pyodide.runPythonAsync(code);
          document.getElementById('output').innerText = result || 'Execution completed.';
        } catch (err) {
          document.getElementById('output').innerText = err;
        }
      });
    } catch (err) {
      document.getElementById('pyodide-loading').innerText = 'Failed to load Pyodide: ' + err;
    }
  }
  main();
</script>
