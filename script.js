// API base URL
const API_URL = '/api';

// Load coffee items when page loads
document.addEventListener('DOMContentLoaded', loadCoffees);

/**
 * Fetch all coffee items from the API
 */
async function loadCoffees() {
    try {
        const response = await fetch(`${API_URL}/coffees`);
        const coffees = await response.json();
        displayCoffees(coffees);
    } catch (error) {
        console.error('Error loading coffees:', error);
        document.getElementById('coffee-list').innerHTML = 
            '<p class="loading">Error loading coffee items. Please try again.</p>';
    }
}

/**
 * Display coffee items in the UI
 */
function displayCoffees(coffees) {
    const coffeeList = document.getElementById('coffee-list');
    
    if (coffees.length === 0) {
        coffeeList.innerHTML = '<p class="loading">No coffee items found.</p>';
        return;
    }
    
    coffeeList.innerHTML = coffees.map(coffee => `
        <div class="coffee-item">
            <div class="coffee-info">
                <div class="coffee-name">${coffee.name}</div>
                <div class="coffee-description">${coffee.description}</div>
            </div>
            <div class="vote-section">
                <div class="vote-count" id="votes-${coffee.id}">${coffee.votes}</div>
                <div class="vote-label">Votes</div>
                <button class="vote-btn" onclick="voteForCoffee(${coffee.id})">
                    👍 Vote
                </button>
            </div>
        </div>
    `).join('');
}

/**
 * Vote for a coffee item
 */
async function voteForCoffee(coffeeId) {
    const voteBtn = event.target;
    voteBtn.disabled = true;
    voteBtn.textContent = '⏳ Voting...';
    
    try {
        const response = await fetch(`${API_URL}/vote`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: coffeeId })
        });
        
        if (response.ok) {
            const data = await response.json();
            // Update the vote count in the UI
            document.getElementById(`votes-${coffeeId}`).textContent = data.votes;
            voteBtn.textContent = '✓ Voted!';
            
            // Re-enable button after a short delay
            setTimeout(() => {
                voteBtn.disabled = false;
                voteBtn.textContent = '👍 Vote';
            }, 1000);
        } else {
            throw new Error('Failed to vote');
        }
    } catch (error) {
        console.error('Error voting:', error);
        voteBtn.disabled = false;
        voteBtn.textContent = '❌ Error';
        
        setTimeout(() => {
            voteBtn.textContent = '👍 Vote';
        }, 2000);
    }
}
