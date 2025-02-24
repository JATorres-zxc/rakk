<template>
  <div class="month-card">
    {{ month }}
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "MonthCard",
  props: {
    month: {
      type: String,
      required: true,
    },
  },
});
</script>

<style scoped>
.month-card {
  border-radius: 10px;
  background-color: #fffefe;
  color: #828282;
  width: 150px;
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  font: 600 24px Inter, sans-serif;
}

@media (max-width: 991px) {
  .month-card {
    width: 100%;
    padding: 0 20px;
  }
}
</style>
