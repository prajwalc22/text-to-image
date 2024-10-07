import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setImage("");

    try {
      const response = await axios.post(
        "http://localhost:8000/generate_image/",
        { prompt }
      );
      setImage(`data:image/png;base64,${response.data.image_data}`);
    } catch (err) {
      setError("Failed to generate image. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold mb-6">Text to Image Generator</h1>
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md bg-white p-6 rounded-lg shadow-md"
      >
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt here"
          className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
        <button
          type="submit"
          className="mt-4 w-full px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Image"}
        </button>
      </form>
      {error && <p className="mt-4 text-red-500">{error}</p>}
      {image && (
        <div className="mt-6">
          <h2 className="text-2xl font-semibold mb-2">Generated Image:</h2>
          <img
            src={image}
            alt="Generated"
            className="max-w-full h-auto border border-gray-300 rounded-lg shadow-md"
          />
        </div>
      )}
    </div>
  );
}
