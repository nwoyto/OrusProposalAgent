import React, { useState } from "react";
import { uploadFile, talkToAgent } from "../services/api";

const Home: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleUpload = async () => {
    if (!file) return;
    const res = await uploadFile(file);
    alert("Uploaded: " + res.filename);
  };

  const handleAgentTalk = async () => {
    const res = await talkToAgent(message);
    setResponse(res.response);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Orus Proposal Agent</h1>

      <div>
        <h2>Upload RFP</h2>
        <input type="file" onChange={e => setFile(e.target.files?.[0] || null)} />
        <button onClick={handleUpload}>Upload</button>
      </div>

      <div style={{ marginTop: 30 }}>
        <h2>Ask the Agent</h2>
        <input
          type="text"
          value={message}
          onChange={e => setMessage(e.target.value)}
          style={{ width: 300 }}
        />
        <button onClick={handleAgentTalk}>Send</button>
        <div><strong>Response:</strong> {response}</div>
      </div>
    </div>
  );
};

export default Home;
