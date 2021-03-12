<script>
    import { getContext } from 'svelte';
    import Button from '@smui/button';

    const { theme, toggle } = getContext('theme');
</script>

<Button on:click={toggle} variant="outlined">{$theme.name}</Button>
