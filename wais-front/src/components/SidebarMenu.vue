<template>
  <nav class="sidebar-menu">
    <img
      src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/e2433d35477616d63912ae308a20a85e61fe58c050f421ac21fd63e5612d5981?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
      alt="Logo"
      class="logo"
    />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/26a852f0243c09a192a5c3f821f69d770983cc608a3f508e9805e4a3ff1848de?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Rice" />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/94a21e3c5cefc112954ca8a64cfcf84da09b4b41fee11300b20c732e06c5b5b4?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Corn" />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/b7303ab62d3af8dda564b4d2e526aac22c852cd52219f05f61ad7809d37aaa56?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Poultry" />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/50177569e27fe550a56ccd12fdd23b528340320a9f4eec7a310ca79f1151492f?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Fish" />
    <img
      src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/ffc0481640c1e254fa7693bb24c3cf3b4ca2b787e126eb46d794fa1d32d6846d?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
      alt=""
      class="decorative-image"
    />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/7d0166109d0a187d0b374afc680a8d4ff00bea749c7466b0d900c8c17272ff4f?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Fruit" />
    <SidebarMenuItem icon="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/d58f65d158b5080c6670aab72ac3002cf902816820ab4f0f49b34642de9f29aa?apiKey=ecf01e10324340c9995a5c95c87db7a5&" label="Spices" />
    <img
      src="https://cdn.builder.io/api/v1/image/assets/ecf01e10324340c9995a5c95c87db7a5/023f94ba144e4c837ed9d8a56cdb4d9370ca6ab0c4a31dd6046238a2fec56022?apiKey=ecf01e10324340c9995a5c95c87db7a5&"
      alt=""
      class="decorative-image"
    />
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SidebarMenuItem from "@/components/SidebarMenuItem.vue";

export default defineComponent({
  name: 'SidebarMenu',
  components: {
    SidebarMenuItem,
  },
});
</script>

<style scoped>
.sidebar-menu {
  margin-top: -79px;
  background-color: #4a6c2f;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  align-items: center;
  color: #f5e8c7;
  width: 124px;
  max-width: 100%;
  padding: 40px 13px;
  font: 300 14px Inter, sans-serif;
}

.logo {
  aspect-ratio: 4.31;
  object-fit: contain;
  object-position: center;
  width: 100%;
  align-self: stretch;
}

.decorative-image {
  aspect-ratio: 1.22;
  object-fit: contain;
  object-position: center;
  width: 66px;
  margin-top: 26px;
}

@media (max-width: 991px) {
  .sidebar-menu {
    white-space: initial;
  }
}
</style>