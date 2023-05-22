<template>
    <a-space direction="vertical">
      <a-input-search
        v-model="value"
        placeholder="input search text"
        style="width: 200px"
        @search="onSearch"
      >
      </a-input-search>
    </a-space>
  </template>
  
  <script scoped>
  import { defineComponent, ref } from 'vue';
  export default defineComponent({
    setup() {
      const value = ref('');
      const onSearch = searchValue => {
        console.log('use value', searchValue);
        console.log('or use this.value', value.value);
      };
      return {
        value,
        onSearch,
      };
    },
  });
  </script>