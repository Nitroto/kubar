<script lang="ts">
    import 'bulma/css/bulma.css';
    import Layout from './components/Layout.svelte';
    import ThemeContext from './components/ThemeContext.svelte';
    import ThemeToggle from './components/ThemeToggle.svelte';
</script>

<ThemeContext>
    <Layout header hideHeader headerHeight={56} let:scroller>
        <div slot="header">
            <div class="header" class:shadow={!!scroller.scroll}>
                Kubar Events Manager
                <ThemeToggle />
            </div>
        </div>
        <main>
            <h1>List of events</h1>
        </main>
        <div slot="footer">
            <div class="footer" class:shadow={!!scroller.scroll}>
                Created by Asen Todorov
            </div>
        </div>
    </Layout>
</ThemeContext>

<style>
    :global(html) {
        background-color: var(--theme-background);
        color: var(--theme-text);
    }

    .header {
        background-color: var(--theme-primary);
        height: 56px;
        line-height: 56px;
        color: white;
        padding-left: 16px;
    }

    .shadow {
        box-shadow: 0 2px 8px #00000088;
    }

    main {
        font-family: sans-serif;
        text-align: center;
    }

    .footer {
        text-align: center;
    }
</style>
