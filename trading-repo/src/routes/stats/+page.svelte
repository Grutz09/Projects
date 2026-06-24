<script>
    import { Chart, registerables } from "chart.js";
    import { supabase } from "$lib/supabase";
    import { onMount } from "svelte";

    Chart.register(...registerables);
    let pnlTrends;
    let accountTrends;
    let winRatio;
    let tradeStats = "totalPnl";
    let newCharts;
        
    async function statistics() {
        const { data: trades, error } = await supabase
            .from('trade-repos')
            .select("*");

        let totalProfits = 0;
        trades.forEach(trade => { totalProfits += trade.profit; });

        let totalLoss = 0;
        trades.forEach(trade => { totalLoss += trade.loss; });


        if(newCharts){
            newCharts.destroy();
        }

        if(tradeStats === "totalPnl"){
            newCharts = new Chart(pnlTrends, {
                type: 'bar',
                data: {
                    labels: ["Total Profits", "Total Loss"],
                    datasets: [{
                        label: 'Profit & Loss',
                        data: [totalProfits, totalLoss],
                        backgroundColor: ['rgba(139, 92, 246, 0.7)', 'rgba(217, 70, 239, 0.7)'],
                        borderColor: ['rgba(139, 92, 246, 1)', 'rgba(217, 70, 239, 1)'],
                        borderWidth: 2,
                        borderRadius: 8,
                    }]
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

        let dates = trades?.map(trade => trade.date);
        let profits = trades?.map(trade => trade.profit);
        let loss = trades?.map(trade => trade.loss);

        if(tradeStats === "accountTrends"){
            newCharts = new Chart(accountTrends, {
                type: 'line',
                data : {
                    labels: dates,
                    datasets: [{data: profits, loss}]
                },
                fill:false,
                backgroundColor: ['rgba(139, 92, 246, 0.7)', 'rgba(217, 70, 239, 0.7)'],
                borderColor: ['rgba(139, 92, 246, 1)', 'rgba(217, 70, 239, 1)']
            })
        }
    }
    onMount(statistics);
</script>

<select name="new-chart" id="new-chart" bind:value={tradeStats} placeholder = "filter">
    <option value="totalPnl">Total PnL</option>
    <option value="accountTrends">Account Trend</option>
    <option value="winRatio">Win Ratio</option>
</select>

<div class="charts-wrapper">
    <canvas class="bar-chart" bind:this={pnlTrends}> </canvas>
</div>

<style>
    .bar-chart {
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
</style>