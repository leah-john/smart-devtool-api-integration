"use client";

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");
  const [useCase, setUseCase] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const analyzeDocumentation = async () => {
    try {
      // Validate inputs
      if (!url.trim()) {
        alert("Please enter a URL");
        return;
      }
      if (!useCase.trim()) {
        alert("Please enter a use case");
        return;
      }

      setLoading(true);
      setResult(null);

      const response = await fetch(
        "http://localhost:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: url.trim(),
            use_case: useCase.trim(),
          }),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();
        console.error("API Error:", errorData);
        alert(`Error: ${errorData.detail || response.statusText}`);
        return;
      }

      const data = await response.json();
      console.log("Analysis Result:", data);
      setResult(data);
    } catch (error) {
      console.error("Full Error:", error);
      if (error instanceof TypeError && error.message.includes("fetch")) {
        alert("Cannot connect to backend. Please ensure the backend server is running on http://localhost:8000");
      } else {
        alert(`Error: ${String(error)}`);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="relative min-h-screen overflow-hidden bg-gradient-to-br from-black via-zinc-950 to-blue-950 text-white px-6 py-12">

      <div className="absolute top-20 left-1/2 -translate-x-1/2 w-[700px] h-[350px] bg-cyan-500/20 blur-[180px] rounded-full"></div>

      <div className="relative max-w-6xl mx-auto">

        <nav className="flex justify-between items-center mb-16">
          <h1 className="text-2xl font-bold">
            Smart DevTool
            <span className="text-cyan-400"> AI</span>
          </h1>

          <div className="text-sm text-gray-400">
            AI-Powered API Integration Assistant
          </div>
        </nav>

        <div className="text-center mb-14">
          <h1 className="text-6xl font-extrabold bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-500 bg-clip-text text-transparent">
            Smart DevTool
          </h1>

          <p className="text-gray-400 text-lg mt-5 max-w-3xl mx-auto leading-relaxed">
            Analyze API documentation, detect authentication methods,
            recommend SDKs, generate wrapper code, and accelerate
            API integration using AI-powered automation.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-12">

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6">
            <div className="text-4xl mb-4">🔍</div>
            <h3 className="text-xl font-bold mb-2">API Detection</h3>
            <p className="text-gray-400">
              Automatically identify providers, endpoints and auth methods.
            </p>
          </div>

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6">
            <div className="text-4xl mb-4">📦</div>
            <h3 className="text-xl font-bold mb-2">SDK Recommendation</h3>
            <p className="text-gray-400">
              Get language-specific SDK suggestions instantly.
            </p>
          </div>

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6">
            <div className="text-4xl mb-4">⚡</div>
            <h3 className="text-xl font-bold mb-2">Wrapper Generation</h3>
            <p className="text-gray-400">
              Generate ready-to-use wrapper classes automatically.
            </p>
          </div>

        </div>

        <div className="max-w-4xl mx-auto mb-12">

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">

            <h2 className="text-3xl font-bold mb-8 text-center">
              Analyze API Documentation
            </h2>

            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Paste your API Dcs URL"
              className="w-full p-4 rounded-xl bg-zinc-900 border border-zinc-700 mb-6"
            />

            <textarea
              rows={5}
              value={useCase}
              onChange={(e) => setUseCase(e.target.value)}
              placeholder="Write your Use-case here"
              className="w-full p-4 rounded-xl bg-zinc-900 border border-zinc-700 mb-6 resize-none"
            />

            <button
              onClick={analyzeDocumentation}
              disabled={loading}
              className="w-full py-4 rounded-xl bg-gradient-to-r from-blue-600 via-cyan-500 to-purple-600 font-bold"
            >
              {loading
                ? "⏳ Analyzing Documentation..."
                : "🚀 Analyze Documentation"}
            </button>

          </div>

        </div>

        <div className="max-w-4xl mx-auto">

          <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8">

            <h2 className="text-3xl font-bold mb-8">
              Analysis Results
            </h2>

            {!result ? (

              <div className="text-center py-16">
                <div className="text-7xl mb-4">📊</div>
                <h3 className="text-2xl font-semibold">
                  No Analysis Yet
                </h3>
                <p className="text-gray-400 mt-2">
                  Analyze documentation to see results.
                </p>
              </div>

            ) : (

              <div className="space-y-6">

                <div className="grid md:grid-cols-2 gap-6">

                  <div className="bg-zinc-900/60 p-5 rounded-xl">
                    <h3 className="text-cyan-400 font-bold mb-2">
                      Provider
                    </h3>
                    <p>{result.provider}</p>
                  </div>

                  <div className="bg-zinc-900/60 p-5 rounded-xl">
                    <h3 className="text-cyan-400 font-bold mb-2">
                      Authentication
                    </h3>
                    <p>{result.authentication}</p>
                  </div>

                </div>

                <div className="bg-zinc-900/60 p-5 rounded-xl">
                  <h3 className="text-cyan-400 font-bold mb-3">
                    Recommended SDKs
                  </h3>

                  <div className="flex flex-wrap gap-3">
                    {result.recommended_sdks?.map(
                      (sdk: string, index: number) => (
                        <span
                          key={index}
                          className="px-4 py-2 rounded-full bg-cyan-500/20 border border-cyan-500/40"
                        >
                          {sdk}
                        </span>
                      )
                    )}
                  </div>
                </div>

                <div className="bg-zinc-900/60 p-5 rounded-xl">
                  <h3 className="text-cyan-400 font-bold mb-3">
                    Endpoints
                  </h3>

                  <ul className="space-y-2">
                    {result.endpoints?.map(
                      (endpoint: string, index: number) => (
                        <li key={index}>
                          {endpoint}
                        </li>
                      )
                    )}
                  </ul>
                </div>

                <div className="bg-zinc-900/60 p-5 rounded-xl">
                  <h3 className="text-cyan-400 font-bold mb-3">
                    AI Recommendations
                  </h3>

                  <p className="text-gray-300 whitespace-pre-wrap">
                    {result.recommendations}
                  </p>
                </div>

                <a
                  href={`http://127.0.0.1:8000${result.download_url}`}
                  target="_blank"
                  className="block w-full text-center py-4 rounded-xl bg-green-600 hover:bg-green-700 font-bold"
                >
                  📥 Download Wrapper
                </a>

              </div>

            )}

          </div>

        </div>

      </div>

    </main>
  );
}