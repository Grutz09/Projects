<script>
    import { createClient } from '@supabase/supabase-js';
    let pair = $state("");
    let position = $state("");
    let profit = $state("");
    let loss = $state("");
    let result = $state("");
    let chart_link = $state("");
    let notes = $state("");

</script>


<main>
    <!-- Trade Entry Form -->
    <div class="form-container">
        <h2>Trading Journal</h2>

        <form class="trading-form">
            <input
                type="text"
                id="pair"
                placeholder="Trading Pair (e.g. EURUSD)"
                bind:value={pair}
                required
            >

            <label for="position">Position</label>
            <select id="position" bind:value={position} required>
                <option value="">Select Position</option>
                <option value="Buy">Buy</option>
                <option value="Sell">Sell</option>
            </select>

            <input
                type="number"
                id="profit"
                bind:value={profit}
                placeholder="Profit"
                required
            >

            <input
                type="number"
                id="loss"
                bind:value={loss}
                placeholder="Loss"
                required
            >

            <label for="result">Result</label>
            <select id="result" required>
                <option value="">Result</option>
                <option value="Win">Win</option>
                <option value="Loss">Loss</option>
                <option value="Breakeven">Breakeven</option>
            </select>

            <input
                type="url"
                id="chart_link"
                placeholder="Chart Screenshot URL"
            >

            <textarea
                id="notes"
                rows="5"
                placeholder="Trade Notes"
            ></textarea>

            <div class="trading-form button">
                <button type="submit" class="btn-submit">
                    Add Trade
                </button>
            </div>
        </form>
    </div>
</main>

<style>/* Container for the form section */
    .form-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem 1.5rem;
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }
    /* The form card itself (Futuristic Glass Card) */
    .trading-form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1.5rem;                /* Increased gap for better spacing */
        padding: 3rem 2rem;         /* Added padding so elements don't touch the borders */
        
        background: rgba(18, 14, 37, 0.6); 
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 16px;        /* Softer corners for modern look */
        box-shadow: 
            0 10px 30px rgba(0, 0, 0, 0.4), 
            0 0 20px rgba(139, 92, 246, 0.05);
    }
    /* Inputs, Select dropdowns, Textareas */
    input, select, textarea {
        padding: 0.75rem 1rem;
        width: 100%;                /* 100% width with max-width is best for mobile screens */
        max-width: 400px; 
        
        background-color: rgba(9, 5, 20, 0.7); /* Matching your deep background */
        color: var(--text);
        font-size: 1rem;
        
        border: 1px solid rgba(139, 92, 246, 0.25);
        border-radius: 8px;
        outline: none;              /* Removes browser default blue outline */
        
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    /* Focus States (Electric Glow) */
    input:focus, select:focus, textarea:focus {
        border-color: var(--primary); /* Glowing purple border */
        background-color: rgba(139, 92, 246, 0.05); /* Subtle purple background tint */
        box-shadow: 
            0 0 0 3px rgba(139, 92, 246, 0.2), 
            0 0 15px rgba(139, 92, 246, 0.1);
    }
    /* Muted placeholder text color */
    ::placeholder {
        color: rgba(245, 243, 255, 0.35);
    }
    /* Fixes select options styling inside dark mode */
    select option {
        background-color: var(--background-2);
        color: var(--text);
    }
    /* Futuristic Submit Button */
    .trading-form button[type="submit"], 
    .btn-submit {
        width: 100%;
        max-width: 400px;
        padding: 0.8rem 1rem;
        font-size: 1rem;
        font-weight: 600;
        color: #ffffff;
        cursor: pointer;
        
        /* Luminous gradient from Electric Violet to Orchid */
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border: none;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
        
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .trading-form button[type="submit"]:hover,
    .btn-submit:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(217, 70, 239, 0.45); /* Intense glow on hover */
    }
    .trading-form button[type="submit"]:active,
    .btn-submit:active {
        transform: translateY(0);
    }
</style>