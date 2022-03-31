<template>
  <div>
    <v-container>
      <!-- jobsデータをidをキーにしてループさせる -->
      <div v-for="job in jobs" :key="job.pk">
        <!-- 下記のように書くと、{{ job.company_name }}を押すと、詳細へ画面遷移する -->
        <h2>
          <router-link
            :to="{ name: 'job', params: { id: job.id } }"
            class="job-link"
            >{{ job.company_name }}
            <!-- apiから取得した、company_nameを表示 -->
          </router-link>
        </h2>

        <!-- apiから取得した、job_titleを表示 -->
        <p>{{ job.job_title }}</p>
        <hr />
      </div>
      <div class="my-4">
        <p v-show="loadingJobs">...loading...</p>
        <v-btn v-show="next" @click="getJobs" color="success">Load More </v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
  import { apiService } from "../common/api.service.js";
  export default {
    name: "home",
    data() {
      return {
        jobs: [],
        next: null,
        loadingJobs: false,
      };
    },
    methods: {
      getJobs() {
        let endpoint = "/api/jobs/";
        if (this.next) {
          endpoint = this.next;
        }
        this.loadingJobs = true;
        apiService(endpoint).then((data) => {
          this.jobs.push(...data.results);
          this.loadingJobs = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        });
      },
    },
    created() {
      this.getJobs();
      // 画面のタイトル
      document.title = "Job Board";
    },
  };
</script>


<style scoped>
/* scopedを使用することによって、部分的にstyleを適用させることが可能。 */
  .job-link {
    font-weight: bold;
    color: black;
    text-decoration: none;
  }

  .job-link:hover {
    color: #41b883;
  }
</style>