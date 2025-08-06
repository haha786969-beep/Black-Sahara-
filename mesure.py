<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Voice Measurement Recorder</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
    }
    label {
      display: block;
      margin-top: 10px;
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
    }
    #savedData {
      margin-top: 20px;
    }
  </style>
</head>
<body>

  <h2> Voice Measurement Recorder</h2>

  <label for="type">Measurement Type</label>
  <select id="type">
    <option value="Length">Length</option>
    <option value="Width">Width</option>
    <option value="Height">Height</option>
    <option value="Depth">Depth</option>
  </select>

  <label for="value">Value (e.g., 3.5 meters)</label>
  <input type="text" id="value" placeholder="Tap mic and speak...">

  <button onclick="startListening()"> Speak Measurement</button>
  <button onclick="saveMeasurement()"> Save</button>

  <div id="savedData">
    <h4> Saved Measurements:</h4>
    <ul id="dataList"></ul>
  </div>

  <script>
    const valueInput = document.getElementById('value');
    const dataList = document.getElementById('dataList');

    function startListening() {
      if (!('webkitSpeechRecognition' in window)) {
        alert("Your browser doesn't support speech recognition.");
        return;
      }

      const recognition = new webkitSpeechRecognition();
      recognition.lang = 'en-US';
      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        valueInput.value = transcript;
      };

      recognition.onerror = function(event) {
        alert("Error occurred in recognition: " + event.error);
      };

      recognition.start();
    }

    function saveMeasurement() {
      const type = document.getElementById('type').value;
      const value = valueInput.value;

      if (!value) {
        alert("Please enter a measurement.");
        return;
      }

      const entry = `${type}: ${value}`;
      const li = document.createElement('li');
      li.textContent = entry;
      dataList.appendChild(li);

      // Optional: Save to localStorage
      const existing = JSON.parse(localStorage.getItem('measurements') || '[]');
      existing.push(entry);
      localStorage.setItem('measurements', JSON.stringify(existing));

      valueInput.value = '';
    }

    // Load existing data from localStorage
    window.onload = function() {
      const existing = JSON.parse(localStorage.getItem('measurements') || '[]');
      existing.forEach(entry => {
        const li = document.createElement('li');
        li.textContent = entry;
        dataList.appendChild(li);
      });
    }
  </script>

</body>
</html>
