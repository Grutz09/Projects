
const supabaseUrl = 'https://uyvcewrjsghtuwdnvbuh.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5dmNld3Jqc2dodHV3ZG52YnVoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0OTUxMjQsImV4cCI6MjA5NzA3MTEyNH0.AAuHdeDg3sh00e9hJRtHr4oOeSuSXqOPbAz0nCDJ2A8';

const supabase = window.supabase.createClient(
    supabaseUrl,
    supabaseKey
);

window.saveTrades = async function saveTrades(){
    const pair = document.getElementById("pair").value;
    const position = document.getElementById("position").value;
    const profit_loss = document.getElementById("profit_loss").value;
    const result = document.getElementById("result").value;
    const chart_link = document.getElementById("chart_link").value;
    const notes = document.getElementById("notes").value;

    const { error } = await supabase
    .from('trades')
    .insert([
        {
            trading_pair: pair,
            position: position,
            profit_loss: profit_loss,
            result: result,
            chart_link: chart_link,
            notes: notes
        }
    ]);

    if (error) {
        console.error(error);
        alert(error.message);
    } else {
        alert("Trade saved.");
    }

    console.log(window.supabase);
    
}

window.showTrades = async function showTrades(){
    const { data: trades, error} = await supabase
    .from('trades')
    .select("*");

    const tradeList = document.querySelector(".trade-table");

    if (!tradeList){
        console.log("Table body not found in DOM.")
    }

    if (error){
        console.log(error);
        return;
    }

    if (trades === null){
        alert("Trades not found.");
        return;
    }

    if (!trades || trades.length === 0){
        console.log("No trades found.")
        tradeList.innerHTML = "";
        return;
    }

    tradeList.innerHTML = "";

    trades.forEach(trade =>{
        //create table row for each trade history
        const tradeRow = document.createElement("tr");
        tradeRow.innerHTML = `
            <td>${trade.trading_pair ?? ""}</td>
            <td>${trade.position ?? ""}</td>
            <td>${trade.profit_loss ?? ""}</td>
            <td>${trade.result ?? ""}</td>
            <td>${trade.chart_link ?? ""}</td>
            <td>${trade.notes ?? ""}</td>
        `;

        tradeList.appendChild(tradeRow);
    })
}

showTrades()