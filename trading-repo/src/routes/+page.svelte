<script>
	import { supabase } from '$lib/supabase';
	let pairs = $state('');
	let position = $state('');
	let profit = $state('');
	let loss = $state('');
	let result = $state('');
	let chart_link = $state('');

	async function addTrade(e) {
		e.preventDefault();

		let trade = {
			pairs: pairs,
			position: position,
			profit: profit,
			loss: loss,
			result: result,
			chart_link: chart_link
		};

		const { error } = await supabase.from('trade-repos').insert(trade).select();

		if (error) {
			console.log(error);
			return;
		} else {
			alert('Trade saved.');
		}
	}
</script>

<main>
	<!-- Trade Entry Form -->
	<div class="form-container">
		<h2>Trading Journal</h2>

		<form class="trading-form" onsubmit={addTrade}>
			<input
				type="text"
				id="pair"
				placeholder="Trading Pair (e.g. EURUSD)"
				bind:value={pairs}
				required
			/>

			<label for="position" class="sr-only">Position</label>
			<select id="position" bind:value={position} required>
				<option value="">Position</option>
				<option value="Buy">Buy</option>
				<option value="Sell">Sell</option>
			</select>

			<input type="number" id="profit" bind:value={profit} placeholder="Profit" required />

			<input type="number" id="loss" bind:value={loss} placeholder="Loss" required />

			<label for="result" class="sr-only">Result</label>
			<select id="result" bind:value={result} required>
				<option value="">Result</option>
				<option value="Win">Win</option>
				<option value="Loss">Loss</option>
				<option value="Breakeven">Breakeven</option>
			</select>

			<input
				type="url"
				id="chart_link"
				bind:value={chart_link}
				placeholder="Chart Screenshot URL"
			/>

			<!-- Fixed class name here to prevent inheriting form card styles -->
			<div class="form-btn-container">
				<button onclick={addTrade} type="submit" class="btn-submit"> Add Trade </button>
			</div>
		</form>
	</div>
</main>

<style>
	/* Container expanded to full-width */
	.form-container {
		width: 100%;
		max-width: 100%;
		padding: 2rem 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
		box-sizing: border-box;
	}

	h2 {
		display: block;
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Courier', serif;
		unicode-bidi: isolate;
		text-align: center;
	}
	/* The form card itself (Futuristic Glass Card as a Grid Row) */
	.trading-form {
		display: grid;
		/* Proportional column ratios:
           Pair (1.5x width), Position (1x), Profit (1x), Loss (1x), Result (1x), Chart Link (2.3x), Button (1.2x) */
		grid-template-columns: 1.5fr 1fr 1fr 1fr 1fr 2.3fr 1.2fr;
		align-items: center;
		gap: 0.75rem; /* Tightened gap slightly to save horizontal space */
		padding: 1.25rem 1.5rem; /* Sleek row-level padding */
		width: 100%;
		box-sizing: border-box;

		background: rgba(50, 39, 106, 0.6);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);

		border: 1px solid rgba(139, 92, 246, 0.2);
		border-radius: 16px;
		box-shadow:
			0 10px 30px rgba(0, 0, 0, 0.4),
			0 0 20px rgba(139, 92, 246, 0.05);
	}

	/* Completely hide labels in desktop grid view to free up columns */
	.trading-form label {
		display: none !important;
	}

	/* Screen Reader Only helper */
	.sr-only {
		position: absolute;
		width: 1px;
		height: 1px;
		padding: 0;
		margin: -1px;
		overflow: hidden;
		clip: rect(0, 0, 0, 0);
		border: 0;
	}

	/* Inputs, Select dropdowns */
	input,
	select {
		padding: 0.75rem 1rem;
		width: 100%;
		max-width: 100%; /* Ensure elements stretch to fill their column cells */
		box-sizing: border-box;

		background-color: rgba(9, 5, 20, 0.7);
		color: var(--text);
		font-size: 0.95rem;

		border: 1px solid rgba(139, 92, 246, 0.25);
		border-radius: 8px;
		outline: none;

		transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
	}

	/* Focus States (Electric Glow) */
	input:focus,
	select:focus {
		border-color: var(--primary);
		background-color: rgba(139, 92, 246, 0.05);
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

	/* Form submit button container cell */
	.form-btn-container {
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	/* Futuristic Submit Button */
	.btn-submit {
		width: 100%;
		padding: 0.8rem 1rem;
		font-size: 0.95rem;
		font-weight: 600;
		color: #ffffff;
		cursor: pointer;

		background: linear-gradient(135deg, var(--primary), var(--secondary));
		border: none;
		border-radius: 8px;
		box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);

		transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
	}

	.btn-submit:hover {
		transform: translateY(-2px);
		box-shadow: 0 6px 20px rgba(217, 70, 239, 0.45);
	}

	.btn-submit:active {
		transform: translateY(0);
	}

	/* Mobile Responsive Stack */
	@media (max-width: 1024px) {
		.trading-form {
			grid-template-columns: 1fr;
			padding: 2.5rem 2rem;
			gap: 1.5rem;
		}

		.trading-form label:not(.sr-only) {
			display: block;
			color: var(--text);
			font-size: 0.9rem;
			align-self: flex-start;
			margin-bottom: -0.75rem;
			margin-left: 0.5rem;
		}

		input,
		select,
		.form-btn-container {
			max-width: 400px;
		}
	}
</style>
