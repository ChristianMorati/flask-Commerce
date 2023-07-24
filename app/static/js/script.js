class DataPreview{
    constructor()
    {
        this.description
        this.url
        this.product_value
    }

    setDescription()
    {
        this.description = document.querySelector('#description').value;
        document.querySelector('#card-description').innerHTML = this.description
    }

    setProduct_value()
    {
        this.product_value = Number(document.querySelector('#product_value').value);
        document.querySelector('#card-price').innerHTML = "R$ " + this.product_value;
    }

    setUrl()
    {
        this.url = document.querySelector('#url').value;
        document.querySelector('#card-url').innerHTML = this.url;
    }
}

const data_preview = new DataPreview();

const ids = ['description', 'url']
ids.forEach((id)=> {
    function_name = 'set' + id[0].toUpperCase() + id.slice(1).toLowerCase()
    console.log(function_name)
    document.getElementById(`${id}`).addEventListener('keyup', data_preview.function_name)
})
document.querySelector('#product-value').addEventListener('keyup', data_preview.setProduct_value)
