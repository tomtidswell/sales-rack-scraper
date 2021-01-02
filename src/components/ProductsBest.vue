<template>
  <section class="products">
    <div class="section">
      <div class="columns">
        <div class="column">
          <div class="subtitle">Browse our best deals</div>
        </div>
      </div>
    </div>
    <article class="columns section">
      <div class="column is-8 product-bubble">
        <div class="subtitle">Kitchen deals</div>
        <div class="scroller-wrap">
          <div class="scroller-content is-flex">
            <Product
              v-for="product in productData.slice(0, 8)"
              class="best-product"
              :data="product"
              :key="product._id"
            />
            <div class="more button is-primary is-rounded is-outlined">More</div>
            <div class="spacer"></div>
          </div>
        </div>
      </div>
    </article>
    <article class="columns section">
      <div class="column is-8 is-offset-4 product-bubble">
        <div class="subtitle">Homeware deals</div>
        <div class="scroller-wrap">
          <div class="scroller-content is-flex">
            <Product
              v-for="product in productData.slice(0, 8)"
              class="best-product"
              :data="product"
              :key="product._id"
            />
            <div class="more button is-primary is-rounded is-outlined">More</div>
            <div class="spacer"></div>
          </div>
        </div>
      </div>
    </article>
  </section>
</template>

<script>
import Product from "./Product.vue";

export default {
  name: "ProductsBest",
  components: {
    Product,
  },
  props: {},
  data() {
    return {
      message: "Hello",
      productData: [],
    };
  },
  created() {
    this.getData();
  },
  computed: {
    csvData: function () {
      return ""; //this.$papa.parse('../../data/marksandspencer-home.csv', {delimiter: ",", newline: ""})
    },
  },
  watch: {},
  methods: {
    async getData() {
      const res = await fetch("./products");
      console.log("Endpoint response:", res);
      this.productData = res.status === 200 ? await res.json() : [];
      console.log("Data:", this.productData);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
a {
  color: #42b983;
}
.subtitle {
  font-size: 1.8rem;
}
section.products {
  display: flex;
  flex-direction: column;
}
.product-bubble {
  padding: 10px 20px;
  background-color: white;
  border-radius: 10px;
  .subtitle{
    margin: 0;
    font-size: 1.5em;
  }
}
article {
  /* max-width: 100%; */
  .scroller-wrap {
    overflow-x: auto;
    padding: 14px;
  }
  .scroller-content {
    max-width: 100%;
  }
  .best-product {
    min-width: 150px;
    margin-right: 15px;
    &:last-child {
      margin-right: 20px;
    }
  }
  .more{
    align-self: center;
  }
  .spacer{
    padding: 10px;
  }
}
</style>
