<template>
  <div class="container">
    {{ msg }}
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'https://felipecps.pythonanywhere.com/hora_atual';
      axios.get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
