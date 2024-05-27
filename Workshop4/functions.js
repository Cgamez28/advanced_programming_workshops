async function callMessage() {
    try {
        //se corrigio la URL, ya que el proyecto si se ejecuta en el localhost, pero lo hace en el puerto 8000
        const response = await fetch('http://localhost:8000/hello_ud'); 
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callWebService() {
    try {
        // ajuste en la URL del servicio
        const response = await fetch('http://localhost:8000/get_products'); 
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Se añade una función para manejar el envío del formulario y enviar la solicitud POST a la API

document.getElementById('productForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;

    try {
        const response = await fetch('http://localhost:8000/create_products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, description })
        });

        if (response.ok) {
            document.getElementById('result').textContent = 'Product added successfully!';
        } else {
            document.getElementById('result').textContent = 'Failed to add product.';
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
