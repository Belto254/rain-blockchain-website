const axios = require('axios');

async function getLivePrices() {
    try {
        const response = await axios.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd');
        const bitcoinPrice = response.data.bitcoin.usd;
        const ethereumPrice = response.data.ethereum.usd;
        console.log(`Current Bitcoin Price: $${bitcoinPrice}`);
        console.log(`Current Ethereum Price: $${ethereumPrice}`);
        document.getElementById('bitcoin-price').innerText = `Current Bitcoin Price: $${bitcoinPrice}`;
        document.getElementById('ethereum-price').innerText = `Current Ethereum Price: $${ethereumPrice}`;
    } catch (error) {
        console.error(error);
    }
}

getLivePrices();
