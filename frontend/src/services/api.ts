export async function uploadFile(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("http://localhost:8000/upload/", {
    method: "POST",
    body: formData,
  });

  return await res.json();
}

export async function talkToAgent(message: string) {
  const res = await fetch("http://localhost:8000/agent/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  return await res.json();
}
