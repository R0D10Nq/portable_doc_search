// Vue 3 приложение через CDN
const { createApp } = window.Vue;

createApp({
  data() {
    return {
      query: "",
      results: [],
      loading: false,
      error: "",
      searched: false,
    };
  },
  methods: {
    async doSearch() {
      this.error = "";
      const q = (this.query || "").trim();
      this.searched = true;
      if (!q) {
        this.results = [];
        return;
      }
      this.loading = true;
      try {
        const resp = await fetch(`/api/search?q=${encodeURIComponent(q)}&k=20`);
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const data = await resp.json();
        this.results = data.results || [];
      } catch (e) {
        console.error(e);
        this.error = "Ошибка запроса. Проверьте логи сервера.";
      } finally {
        this.loading = false;
      }
    },
  },
}).mount("#app");
