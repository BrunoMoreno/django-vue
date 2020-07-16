<template>
  <div class="row">
    <div class="col-md-8" >
      <div v-for="tutorial in tutorials" v-bind:key="tutorial.id">
        <h5>{{ tutorial.title }}</h5>
        <p>{{ tutorial.description }}</p>
        <small>
          {{ tutorial.created_at}}
        </small>
        <hr>
      </div>      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {

  data() {
    return {
      tutorials: []
    }
  },

  mounted: function () {
    this.getTutorials()
  },

  methods: {
    getTutorials: async function () {
      await axios.get('http://localhost:8000/api/tutorials')
      .then((res) => {
        this.tutorials = res.data
        console.log(res.data)
      })
      .catch((e) => {
        console.log(e)
      })
    }
  }
}
</script>