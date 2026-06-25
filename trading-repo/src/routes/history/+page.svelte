<script>
	import { supabase } from '$lib/supabase';
    import {onMount} from 'svelte';
    
    let tradeHistory;
    async function showTradeHistory(){
        const {data: trades, error } = await supabase
        .from('trade-repos')
        .select("*");

        if(error){
            console.log(error);
            alert("Error encountered.");
            return;
        }

        if(!trades || trades.length === 0){
            console.log("No trades found.");
            tradeHistory.innerHTML = "";
            return;
        }

        trades.forEach(trade => {
            // create rows for each trade
            const tradeRow = document.createElement("tr");
            tradeRow.innerHTML = `
                <td>${trade.pairs ?? ""}</td>
                <td>${trade.position ?? ""}</td>    
                <td>${trade.profit ?? ""}</td>
                <td>${trade.loss ?? ""}</td>
                <td>${trade.result ?? ""}</td>
                <td>${trade.chart_link ?? ""}</td>
            `;
            tradeRow.classList.add("trade-row");
            tradeHistory.appendChild(tradeRow);
        });
    }

    onMount(showTradeHistory);
</script>

<main>
	<div class="main-container">
		<h1>Trade History</h1>
		<div class="trade-container">
			<table>
				<thead>
					<tr>
						<th>Pair</th>
						<th>Position</th>
						<th>Profit</th>
                        <th>Loss</th>
						<th>Result</th>
						<th>Chart</th>
					</tr>
				</thead>

				<tbody class="trade-table" bind:this={tradeHistory}>
					<!-- Trades will be added here -->
				</tbody>
			</table>
		</div>
	</div>
</main>

<style>
    main{
        flex:1;
    }
	.main-container {
		width: 100%;
		max-width: 100%;
		padding: 2rem 1.5rem;
		box-sizing: border-box;
	}
	.trade-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 10px;
		margin: 0 30px 0 30px;
		/* Change from pure black to a deep dark purple gradient */
		background: rgba(50, 39, 106, 0.6);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		border: 1px solid rgba(139, 92, 246, 0.2);
		border-radius: 16px;
		box-shadow:
			0 10px 30px rgba(0, 0, 0, 0.4),
			0 0 20px rgba(139, 92, 246, 0.05);

		border-radius: 14px;
		padding: 30px;

		font-family: sans-serif;
		color: #ffffff;
	}

	/* 2. Style the Title */
	h1 {
		margin: 0 0 5px 0;
		font-size: 1.8rem;
		font-family: 'Courier', sans-serif;
		letter-spacing: 0.2px;
		padding-bottom: 10px;
		text-align: center;
	}

	/* 3. Strip the harsh lines and format the table structure */
	table {
		width: 100%;
		border-collapse: collapse; /* This removes the double-border spacing */
		text-align: center;
	}

	/* 4. Headers: subtle semi-transparent background */
	th {
		padding: 16px;
		font-size: 12px;
		font-weight: 700;
		letter-spacing: 1px;
		color: rgba(255, 255, 255, 0.6);
		background-color: rgba(255, 255, 255, 0.05);
		border-bottom: 2px solid rgba(255, 255, 255, 0.1);
	}

	/* 5. Table Rows: Soft divider lines instead of harsh boxes */
	:global(.trade-row td){
		padding: 16px;
		font-size: 14px;
		color: rgba(255, 255, 255, 0.9);
		/* Soft dividers instead of full boxes */
		border-bottom: 1px solid rgba(255, 255, 255, 0.05);
	}

    :global(.trade-row td:hover){
        background-color: rgba(255, 255, 255, 0.07);
		cursor: pointer;
    }

	/* 6. Premium Row Hover Effect */
	.trade-container tr:hover {
		background-color: rgba(255, 255, 255, 0.07);
		cursor: pointer;
	}
	table,
	th{
		padding: 10px;
	}
</style>
