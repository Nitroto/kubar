import { ApolloClient, InMemoryCache } from '@apollo/client';
import { setClient } from 'svelte-apollo';

const apolloClient = () => {
    const client = new ApolloClient({
        cache: new InMemoryCache(),
        uri: 'http://localhost:8000/graphql',
        headers: {
            authorization: localStorage.getItem('token') || '',
            'client-name': 'Kubar [web]',
            'client-version': '1.0.0',
        },
    });
    setClient(client);
};

export default apolloClient;
