<script>
	import '../app.css';
	import logo from '$lib/assets/trading-repo logo.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={logo} />
</svelte:head>

<nav>
	<a class="logo" href="/"> <img src="{logo}" alt="logo"></a>
	<div class = "navWrapper">
		<a href="/">Trade Form</a>
		<a href="/../history">History</a>
		<a href="/../stats">Statistics</a>
	</div>
</nav>

<hr class="divider" />

{@render children()}

<footer class="footer">
	<p>© 2026 Trading Repo. All rights reserved.</p>
</footer>

<style>
	nav,
	.navWrapper,
	.footer{
		display: flex;
	}

	.logo img{
		width: 150px;
		height: 150px;
		border-radius: 50%;
	}

	nav {
		justify-content: center;
		align-items: center;
		padding: 0.5rem 2rem;
		background-color: var(--accent);
	}

	.navWrapper, .navWrapper a{
		margin-left: 1.5rem;
		text-decoration: none;
		color: var(--text);
		padding-right: 10px;
	}

	a{
		padding: 10px 15px 10px 15px;
		border: 2px solid transparent; /* Add this line */
	}

	a:hover {
		color: var(--text);
		background-color: var(--secondary);
		border-radius: 2px;
		border: 2px solid var(--background);
	}

	.divider {
		border: none;
		border-top: 1px solid var(--accent);
		margin: 0;
	}

	.footer {
		justify-content: center;
		align-items: center;
		padding: 1rem;
		background-color: var(--accent);
		color: var(--text);
	}
</style>
