import React, { useState } from 'react';
import './App.css';

function App() {
  // Define state variables for file upload and question-answering
  const [fileType, setFileType] = useState('');
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  // Handle file upload
  const handleFileUpload = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('file', e.target.files[0]);

    try {
      const response = await fetch('http://127.0.0.1:8000/upload_files', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setFileType(`File Type: ${data.file_type}`);
      } else {
        setFileType('Error uploading file.');
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Handle question answering
  const handleQuestionAnswering = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:8000/api/your-ml-endpoint', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });

      if (response.ok) {
        const data = await response.json();
        setAnswer(`Answer: ${data.answer}`);
      } else {
        setAnswer('Error getting answer.');
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        {/* File Upload Form */}
        <input type="file" onChange={handleFileUpload} />
        <p>{fileType}</p>

        {/* Question Answering Form */}
        <form onSubmit={handleQuestionAnswering}>
          <label htmlFor="query">Enter your question:</label>
          <input
            type="text"
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            required
          />
          <button type="submit">Get Answer</button>
        </form>
        <p>{answer}</p>
      </header>
    </div>
  );
}

export default App;
