<template>
  <div class="calendar-grid">
    <div class="year-selector">
      <img
        src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/32ea1d8665726844c5206762727206bd7375115415a6a2f039a4a907ff22e720?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
        alt="Previous year"
        class="year-nav-icon"
      />
      <div class="year">2025</div>
      <img
        src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/26e91e6d8b9efd4a5c86289ed0f25fec94d5497381b0f5f14890317f7985f747?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
        alt="Next year"
        class="year-nav-icon"
      />
    </div>
    <div class="months-grid">
      <MonthCard v-for="month in months" :key="month" :month="month" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MonthCard from "@/components/MonthCard.vue";

export default defineComponent({
  name: "CalendarGrid",
  components: {
    MonthCard,
  },
  data() {
    return {
      months: [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
      ],
    };
  },
});
</script>

<style scoped>
.calendar-grid {
  background-color: rgba(207, 223, 218, 0.5);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  align-items: center;
  padding: 44px 80px 71px;
}

.year-selector {
  display: flex;
  width: 184px;
  max-width: 100%;
  gap: 20px;
  color: #000;
  justify-content: space-between;
  font: 900 17px Inter, sans-serif;
  margin-bottom: 19px;
}

.year-nav-icon {
  aspect-ratio: 1;
  object-fit: contain;
  object-position: center;
  width: 48px;
  cursor: pointer;
}

.months-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px 20px;
}

@media (max-width: 991px) {
  .calendar-grid {
    max-width: 100%;
    padding: 0 20px;
  }

  .months-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .months-grid {
    grid-template-columns: 1fr;
  }
}
</style>
