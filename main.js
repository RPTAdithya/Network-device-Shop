let allProducts = [];

fetch("http://127.0.0.1:5000/products")
.then(res => res.json())
.then(data => {
    allProducts = data;
    displayProducts(allProducts);
});

function displayProducts(products) {
    let html = "";
    products.forEach(p => {
        html += `
        <div class="product">
            <h3>${p.name}</h3>
            <p>${p.category}</p>
            <p>Rs. ${p.price}</p>
            <button onclick="buyProduct('${p.name}')">Buy</button>
        </div>`;
    });
    document.getElementById("products").innerHTML = html;
}

function showProducts(category) {
    if (category === 'all') {
        displayProducts(allProducts);
    } else {
        displayProducts(allProducts.filter(p => p.category === category));
    }
}

function buyProduct(name) {
    alert(name + " added to cart!");
}

// Contact form
document.getElementById("contactForm").addEventListener("submit", function(e){
    e.preventDefault();

    fetch("http://127.0.0.1:5000/contact", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({
            name: name.value,
            email: email.value,
            message: message.value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
});
