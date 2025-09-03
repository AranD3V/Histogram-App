// --- Backend for Histopathology Image Classifier ---
// This server handles API requests and serves the frontend application.

// 1. Import Dependencies
const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');

// 2. Initialize Express App
const app = express();
// Heroku/Render will provide a port via an environment variable. Fallback to 3000 for local dev.
const PORT = process.env.PORT || 3000; 

// 3. Configure Middleware
app.use(cors()); // Enable CORS

// Serve the static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Configure Multer for file uploads (in-memory storage)
const upload = multer({ storage: multer.memoryStorage() });

// 4. Define the API Endpoint for Classification
app.post('/classify', upload.single('image'), (req, res) => {
    console.log('Received a request to /classify');
    if (!req.file) {
        console.log('No file uploaded.');
        return res.status(400).json({ error: 'No image file provided.' });
    }

    console.log(`File received: ${req.file.originalname}, size: ${req.file.size} bytes`);

    // --- SIMULATED MODEL INFERENCE ---
    console.log('Simulating model inference...');
    setTimeout(() => {
        const isMalignant = Math.random() > 0.5;
        const confidence = 85 + Math.random() * 14;

        const result = {
            prediction: isMalignant ? 'Malignant' : 'Benign',
            confidence: confidence.toFixed(2),
            classColor: isMalignant ? 'red' : 'green',
            recommendation: isMalignant 
                ? 'High probability of malignancy detected. Urgent review recommended.' 
                : 'Low probability of malignancy detected. Routine follow-up suggested.'
        };

        console.log('Simulation complete. Sending result:', result);
        res.status(200).json(result);
    }, 2000); 
});

// 5. Define a catch-all route to serve the frontend
// This ensures that refreshing the page on any sub-route will still load the index.html
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// 6. Start the Server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    console.log('Ready to accept image classification requests.');
});