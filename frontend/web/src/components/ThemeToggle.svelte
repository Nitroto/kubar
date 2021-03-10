<script>
    import { getContext } from 'svelte';
    import { Button } from 'svelma';

    const { theme, toggle } = getContext('theme');
</script>

<Button on:click={toggle}>{$theme.name}</Button>
