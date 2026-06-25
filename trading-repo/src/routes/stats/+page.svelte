<script>
	import { Chart, registerables } from 'chart.js';
	import { supabase } from '$lib/supabase';
	import { onMount } from 'svelte';

	Chart.register(...registerables);

	let pnlTrends;
	let accountTrends;
	let winRatio;
	let tradeStats = $state('totalPnl');
	let newCharts;

	let allTrades = [];

    // reruns the main function whenever there's a reactive code. (e.g count or submit – makes changes to the website)
	$effect(() => {
		console.log(tradeStats);
		if (allTrades.length < 1) return;
		statistics();
	});

    // fetches the datas on database - it avoids repeated fetching of data and instead stores it into a variable
	async function fetchTrade() {
		const { data: trades, error } = await supabase.from('trade-repos').select('*');
		allTrades = trades;
		statistics();
	}

    // consists of 3 visual graphs and their logic
	async function statistics() {
        // destroys the old graph whenever user changes filter to replace it
		if (newCharts) {
			newCharts.destroy();
		}

        if (tradeStats === 'totalPnl'){
            createBarchart();
        }

        if (tradeStats === 'accountTrends'){
            createLineChart();
        }

        if (tradeStats === 'winRatio'){
            createPieChart();
        }
        
    }

    async function createBarchart() {
        let totalProfits = 0;
		allTrades.forEach((trade) => {
			totalProfits += trade.profit ?? 0;
		});

		let totalLoss = 0;
		allTrades.forEach((trade) => {
			totalLoss += trade.loss ?? 0;
		});

		newCharts = new Chart(pnlTrends, {
				type: 'bar',
				data: {
					labels: ['Total Profits', 'Total Loss'],
					datasets: [
						{
							label: 'Profit & Loss',
							data: [totalProfits, totalLoss],
							backgroundColor: ['rgba(139, 92, 246, 0.7)', 'rgba(217, 70, 239, 0.7)'],
							borderColor: ['rgba(139, 92, 246, 1)', 'rgba(217, 70, 239, 1)'],
							borderWidth: 2,
							borderRadius: 8
						}
					]
				},
				options: {
					plugins: {
						legend: { labels: { color: '#f5f3ff' } }
					},
					scales: {
						x: { ticks: { color: '#f5f3ff' }, grid: { display: false } },
						y: { ticks: { color: '#f5f3ff' }, grid: { color: 'rgba(139, 92, 246, 0.1)' } }
					}
				}
			});
		}

    async function createLineChart(){
        // variables for line chart
        let validTrades = allTrades?.filter(
            (trade) => trade.profit != null || trade.loss != null
        );

        let dates = validTrades?.map((trade) =>
            new Date(trade.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
        );

        let rawPnl = validTrades.map((trade) => (trade.profit ?? 0) - (trade.loss ?? 0));
        let pnl = rawPnl.reduce((acc, val, i) => {
            acc.push((acc[i - 1] ?? 0) + val);
            return acc;
        }, []);

		console.log(dates, pnl);
		newCharts = new Chart(accountTrends, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    data: pnl,
                    backgroundColor: 'rgba(139, 92, 246, 0.15)',
                    borderColor: 'rgba(139, 92, 246, 1)',
                    borderWidth: 2,
                    tension: 0.4,
                    fill: true,
                    pointRadius: 0,        
                    pointHoverRadius: 5, 
                }]
            },
            options: {
                plugins: {
                    legend: { display: false }  
                },
                scales: {
                    x: {
                        ticks: { color: '#888', maxTicksLimit: 7 },
                         grid: { display: false },
                        border: { display: false }
                        },
                    y: {
                        min: 0,
                        ticks: { color: '#888' },
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        border: { display: false }
                    }
                }
            }
        });
    }

    async function createPieChart(){
        if(allTrades.length === 0) return;
        let win = allTrades.filter((trades) => trades.result === "Win");
        let loss = allTrades.filter((trades) => trades.result === "Loss");
        let winRate = (win.length/allTrades.length) * 100;
        let lossRate = (loss.length/allTrades.length) * 100;

        newCharts = new Chart(winRatio, {
            type: 'pie',
            data: {
                labels: ['Win', 'Loss'],
                datasets: [{
                    data: [winRate, lossRate],
                    backgroundColor: ['rgba(139, 92, 246, 0.7)', 'rgba(217, 70, 239, 0.7)'],
                    borderColor: ['rgba(139, 92, 246, 1)', 'rgba(217, 70, 239, 1)'],
                    borderWidth: 2
                }]
            },
            options: {
                plugins: {
                    legend: {
                        labels: { color: '#f5f3ff' }
                    }
                }
            }
        });
    }

	onMount(fetchTrade);
</script>

<main class="stat-container">
	<div class="filter-container">
		<label for="new-chart">Filter:</label>
		<select name="new-chart" id="new-chart" bind:value={tradeStats} placeholder="filter">
			<option value="totalPnl">Total PnL</option>
			<option value="accountTrends">Account Trend</option>
			<option value="winRatio">Win Ratio</option>
		</select>
	</div>

	<div class="charts-wrapper">
		<div style={tradeStats !== 'totalPnl' ? 'display:none' : ''}>
			<canvas class="bar-chart" bind:this={pnlTrends}></canvas>
		</div>
		<div style={tradeStats !== 'accountTrends' ? 'display:none' : ''}>
			<canvas class="line-chart" bind:this={accountTrends}></canvas>
		</div>

        <div style={tradeStats !== 'winRatio' ? 'display:none' : ''}>
			<canvas class="pie-chart" bind:this={winRatio}></canvas>
		</div>
	</div>
</main>

<style>
	.bar-chart {
		width: 700px !important;
		height: 400px !important;
		padding: 0.75rem;
		border-radius: 12px;
		background: rgba(18, 14, 37, 0.6);
		border: 1px solid rgba(139, 92, 246, 0.2);
	}

	.line-chart {
		width: 700px !important;
		height: 400px !important;
		padding: 0.75rem;
		border-radius: 12px;
		background: rgba(18, 14, 37, 0.6);
		border: 1px solid rgba(139, 92, 246, 0.2);
	}
	.charts-wrapper {
		display: flex;
		gap: 1rem;
		justify-content: center;
		align-items: flex-start;
	}

    .filter-container{
        display: flex;
        flex-direction: row;
        justify-content: end;
        padding: 0px 20px 20px 20px;
        align-items: center;
        font-size: medium;
        gap: 8px;
    }

    #new-chart {
        background-color: rgba(18, 14, 37, 0.8);
        color: #f5f3ff;
        border: 1px solid rgba(139, 92, 246, 0.4);
        border-radius: 8px;
        padding: 6px 12px;
        cursor: pointer;
        outline: none;
    }

    #new-chart:focus {
        border-color: rgba(139, 92, 246, 1);
    }
</style>
