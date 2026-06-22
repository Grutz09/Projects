<script>
	import '../app.css';
	import logo from '$lib/assets/trading-repo logo.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={logo} />
</svelte:head>

<nav>
	<div class="logo">
		<img src="{logo}" alt="Trading Repo Logo" />
		<span>Trading Repo</span>
	</div>
	
	<div class = "navWrapper">
		<a href="/">Trade Form</a>
		<a href="/../history">History</a>
		<a href="/../stats">Statistics</a>
	</div>
</nav>

<hr class="divider" />

{@render children()}

<footer class="footer">
  <!-- Optional footer links for a premium layout -->
  <div class="footer-links">
    <a href="/privacy">Privacy Policy</a>
    <a href="/terms">Terms of Service</a>
    <a href="/contact">Contact</a>
  </div>
  <p>© 2026 Trading Repo. All rights reserved.</p>
</footer>

<style>
	nav,
	.navWrapper,
	.footer{
		display: flex;
	}

	.logo{
		display: flex;
  		align-items: center;
  		gap: 0.75rem;
	}

	.logo img{
		width: 42px;                  /* Reduced from 150px to fit a standard navbar */
  		height: 42px;
  		border-radius: 50%;
  		object-fit: cover;
  		border: 2px solid var(--primary);
  		box-shadow: 0 0 10px rgba(139, 92, 246, 0.3); /* Electric glow around logo */
	}

	nav{
		padding: 0.75rem 1.5rem;
		justify-content: space-between;
	}
	/* Nav Links Wrapper */	
	.navWrapper {
		display: flex;
		align-items: center;
		gap: 0.5rem;                  /* Standard gap spacing between links */
	}
	/* Scoped Nav Links (Won't affect links outside nav) */
	.navWrapper a {
		text-decoration: none;
		color: rgba(245, 243, 255, 0.75); /* Softened white for better hierarchy */
		font-weight: 500;
		padding: 0.6rem 1.1rem;
		border-radius: 6px;
		border: 1px solid transparent;
		transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); /* Smooth micro-animation */
	}
	/* Nav Link Hover State */
	.navWrapper a:hover {
		color: var(--text);
		background-color: rgba(139, 92, 246, 0.1); /* Soft glass pill background hover */
		border-color: rgba(139, 92, 246, 0.25);
	}
	
	/* Premium Gradient Divider */
	.divider {
		border: none;
		height: 1px;
		/* Fades out on the left and right, glowing violet in the center */
		background: linear-gradient(
			90deg, 
			transparent, 
			rgba(139, 92, 246, 0.35) 50%, 
			transparent
		);
		margin: 4rem auto;
		width: 90%; /* Keeps it from stretching completely to the screen edges */
	}

	/* Footer Container */
	.footer {
		padding: 3rem 2rem;
		background-color: rgba(9, 5, 20, 0.9); /* Solidified dark violet backdrop */
		border-top: 1px solid rgba(139, 92, 246, 0.1); /* Subtle top line separation */
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
	}

	/* Footer Utility Links */
	.footer-links {
		display: flex;
		gap: 1.5rem;
	}

	.footer-links a {
		color: rgba(245, 243, 255, 0.5); /* Muted violet-white */
		text-decoration: none;
		font-size: 0.85rem;
		transition: color 0.2s ease;
	}

	.footer-links a:hover {
	 color: var(--secondary); /* Radiant orchid highlight on hover */
	}

	/* Copyright text */
	.footer p {
		color: rgba(245, 243, 255, 0.4); /* Extra muted text for low visual weight */
		font-size: 0.85rem;
		margin: 0;
		letter-spacing: 0.5px;
	}
</style>
