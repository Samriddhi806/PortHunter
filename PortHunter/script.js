document.getElementById('portHunterForm').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const ipAddress = document.getElementById('ipAddress').value;
    const resultsDiv = document.getElementById('results');
  
    // Clear previous results
    resultsDiv.innerHTML = 'Scanning...';
  
    try {
      // Send the IP address to the backend API
      const response = await fetch('/scan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ip: ipAddress }),
      });
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = await response.json();
  
      // Display the results
      if (data.ports && data.ports.length > 0) {
        resultsDiv.innerHTML = '<strong>Open Ports:</strong><br>' + data.ports.join(', ');
      } else {
        resultsDiv.innerHTML = 'No open ports found.';
      }
    } catch (error) {
      resultsDiv.innerHTML = 'Error: ' + error.message;
    }
  });