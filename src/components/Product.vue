<template>
  <div class="product" v-show="lastSeen !== 'Not recently'">
    <a :href="url" class="name">{{name}}</a>
    <div class="line"></div>
    <img class="main" :src="image" >
    <div class="prices">
        <div class="badge" v-if="badge">{{badge}}</div>
        <div class="no-badge" v-else></div>
        {{ price }}
        <span class="prices previous-price" v-if="prevPrice">{{prevPrice}}</span>
    </div>
    <div class="last-seen">⏱{{lastSeen}}</div>
  </div>
</template>

<script>
import {timeDiffToNow} from '../../lib/time'
export default {
  name: 'Products',
  props: {
    data: Object
  },
  data(){
    return{
      message: 'Hello'
    }
  },
  computed: {
    // a computed getter
    name: function () { return this.data.name },
    price: function () { return this.data.latestPrice.price },
    priceDescription: function () { 
        return this.data.latestPrice.priceDescription.replace('Price','').replace('price','').replace('Current','').trim()
    },
    prevPrice: function () { return this.data.prev_price },
    url: function () { return this.data.url },
    badge: function () { return this.data.latestPrice.badge || this.priceDescription },
    image: function () { return this.data.main_image },
    lastSeen: function () { 
        return timeDiffToNow(this.data.updatedAt)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.product{
    position:relative;
    display: flex;
    flex-direction: column;
    box-shadow: 10px 10px 14px 0px #9a9a9a2b, -10px -10px 14px 0px #e2e2e221;
    border-radius: 5px;
    padding: 10px;
    backdrop-filter: blur(7px);
    background-color: #ffffff;
    color: #546E7A;
}
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    text-decoration: none;
    color: #546E7A;
}
img.main{
    width: 100%;
    object-fit: contain;
}
.line{
    height: 1px;
    width: 80%;
    margin: 10px;
    background: #d0d9e0;
    align-self: center;
}
.prices{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 6px;
}
.previous-price{
    text-decoration: line-through;
}
.badge{
    background-color: red;
    position: relative;
    color: white;
    padding: 2px 8px;
    width: fit-content;
}
.last-seen{
    font-size: 0.8em;
    display: flex;
    justify-content: flex-end;
}
</style>
