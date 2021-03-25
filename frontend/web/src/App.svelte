<script lang="ts">
    import { Link, Route, Router } from 'svelte-navigator';
    import Layout from './components/Layout.svelte';
    import ThemeContext from './components/ThemeContext.svelte';
    import ThemeToggle from './components/ThemeToggle.svelte';

    import Home from './components/Home.svelte';
    import About from './components/About.svelte';

    export let url = '';
</script>

<Router url="{url}">
    <ThemeContext>
        <Layout header hideHeader headerHeight={56} let:scroller>
            <div slot="header">
                <nav class="header" class:shadow={!!scroller.scroll}>
                    Kubar Events Manager
                    <Link to="/">Home</Link>
                    <Link to="about">About</Link>
                    <ThemeToggle />
                </nav>
            </div>
            <main>
                <Route path="/" component="{Home}" />
                <Route path="about" component={About} />
            </main>
            <div slot="footer">
                <div class="footer" class:shadow={!!scroller.scroll}>
                    Created by Asen Todorov
                </div>
            </div>
        </Layout>
    </ThemeContext>
</Router>

<style lang="sass">
  \:global(html)
    background-color: var(--theme-background)
    color: var(--theme-text)

  .header
    background-color: var(--theme-primary)
    height: 56px
    line-height: 56px
    color: white
    padding-left: 16px

  .shadow
    box-shadow: 0 2px 8px #00000088

  main
    font-family: sans-serif
    text-align: center

  .footer
    text-align: center
</style>
