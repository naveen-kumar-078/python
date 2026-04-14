const menuItems = [
    {
        id: 1,
        name: 'Espresso',
        description: 'Rich and bold single shot of pure coffee essence',
        price: 3.50,
        category: 'coffee',
        image: 'https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=400'
    },
    {
        id: 2,
        name: 'Cappuccino',
        description: 'Perfect balance of espresso, steamed milk, and foam',
        price: 4.50,
        category: 'coffee',
        image: 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400'
    },
    {
        id: 3,
        name: 'Latte',
        description: 'Smooth espresso with creamy steamed milk',
        price: 4.75,
        category: 'coffee',
        image: 'https://images.unsplash.com/photo-1561882468-9110e03e0f78?w=400'
    },
    {
        id: 4,
        name: 'Americano',
        description: 'Espresso diluted with hot water for a milder taste',
        price: 3.75,
        category: 'coffee',
        image: 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400'
    },
    {
        id: 5,
        name: 'Mocha',
        description: 'Chocolate meets espresso with whipped cream',
        price: 5.25,
        category: 'specialty',
        image: 'https://images.unsplash.com/photo-1578314675249-a6910f80cc39?w=400'
    },
    {
        id: 6,
        name: 'Caramel Macchiato',
        description: 'Vanilla, milk, espresso, and caramel drizzle',
        price: 5.50,
        category: 'specialty',
        image: 'https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=400'
    },
    {
        id: 7,
        name: 'Cold Brew',
        description: 'Slow-steeped for 20 hours, smooth and refreshing',
        price: 4.25,
        category: 'specialty',
        image: 'https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400'
    },
    {
        id: 8,
        name: 'Croissant',
        description: 'Buttery, flaky French pastry',
        price: 3.50,
        category: 'pastry',
        image: 'https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=400'
    },
    {
        id: 9,
        name: 'Blueberry Muffin',
        description: 'Fresh-baked with real blueberries',
        price: 3.75,
        category: 'pastry',
        image: 'https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=400'
    },
    {
        id: 10,
        name: 'Cinnamon Roll',
        description: 'Warm, gooey, with cream cheese frosting',
        price: 4.25,
        category: 'pastry',
        image: 'https://images.unsplash.com/photo-1609127102567-8a9a21dc27d8?w=400'
    }
];

const menuGrid = document.getElementById('menuGrid');
const categoryBtns = document.querySelectorAll('.category-btn');
const navToggle = document.getElementById('navToggle');
const navLinks = document.querySelector('.nav-links');
const contactForm = document.getElementById('contactForm');

function renderMenu(category = 'all') {
    const filtered = category === 'all' 
        ? menuItems 
        : menuItems.filter(item => item.category === category);
    
    menuGrid.innerHTML = filtered.map(item => `
        <div class="menu-item">
            <img src="${item.image}" alt="${item.name}">
            <div class="menu-item-content">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <div class="menu-item-footer">
                    <span class="price">$${item.price.toFixed(2)}</span>
                    <button class="add-btn" onclick="addToCart(${item.id})">Add</button>
                </div>
            </div>
        </div>
    `).join('');
}

categoryBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        categoryBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderMenu(btn.dataset.category);
    });
});

navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

function addToCart(id) {
    const item = menuItems.find(i => i.id === id);
    alert(`${item.name} added to cart!`);
}

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you for your message! We\'ll get back to you soon.');
    contactForm.reset();
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

renderMenu();
