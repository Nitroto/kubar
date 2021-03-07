<script>
    import {getContext} from 'svelte'

    const {theme, toggle} = getContext('theme')
</script>

<button on:click={toggle}>{$theme.name}</button>
