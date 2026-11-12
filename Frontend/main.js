const searchBox = document.getElementById('searchBox');
const searchBtn = document.getElementById('searchBtn');
const resultBox = document.getElementById('resultBox');

searchBtn.addEventListener('click', async () => {
    
    const queryText = searchBox.value.trim();
    
    if (!queryText) {
    resultBox.classList.remove('hidden');
        resultBox.className = "result-display notext-warn";
        resultBox.innerHTML = `Please enter a query before scanning.`;
        return;
    }

    console.log(`Igniting query transmission packet: "${queryText}"`);

    try {
        
        const response = await fetch('http://127.0.0.1:5000/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            
            body: JSON.stringify({
                query: queryText
            })
        });

        const responseData = await response.json();
        console.log("Output data:", responseData);

        resultBox.classList.remove('hidden');

        if (responseData.status === "found") {
            resultBox.className = "result-display result-success";
            resultBox.innerHTML = `<strong>Match Confirmed!</strong><br>"${responseData.match}"`;
} else {
            resultBox.className = "result-display result-fail";
            resultBox.innerHTML = `<strong>Scan Complete:</strong> No matching data assets located.`;
        }

    } catch (networkError) {
        console.error("Critical Network Error:", networkError);
        alert("Failed to connect to the backend logic engine. Ensure the server is running on the correct port;");
    }
});