<template>
  <div class="container">
    <section class="h-100 gradient-custom-2">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col col-lg-9 col-xl-7">
            <div class="card">
              <div class="rounded-top text-white d-flex flex-row" style="background-color: #000; height:200px;">
                <div class="ms-4 mt-5 d-flex flex-column" style="width: 150px;">

                  <div class="image-container" style="width: 150px; height: 180px;">
                    
                    <img v-if="user?.image_base64" :src="getImageSrc(user?.image_base64)"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%; z-index: 2;">
                  
                    <img v-else src="../assets/baseProfile.png"
                      alt="프로필 이미지" class="img-fluid img-thumbnail mt-4 mb-2 py-3"
                      style="max-width: 100%; max-height: 100%; z-index: 1;">
                  </div>
                  
                  <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                    @click="openModal"
                    style="z-index: 1;">
                    Edit profile
                  </button>

                  <!-- Edit Profile Modal -->
                  <div class="modal" tabindex="-1" role="dialog" id="editProfileModal">
                    <div class="modal-dialog" role="document">
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title" style="color: black;">프로필 이미지 변경</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>

                        <div class="modal-body">
                          <form>
                            <div class="mb-3">
                              <label for="profileImg" class="form-label">이미지 업로드</label>
                              <input type="file" class="form-control border" id="profileImg" :v-model="uploadImg" @change="handleFileChange"/>
                              <div>
                                <img class="mt-3" style="width: 100%" v-if="uploadImg" :src="uploadImgUrl" alt="Uploaded Image">
                              </div>
                            </div>
                          </form>
                        </div>

                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="closeEditProfileModal">취소</button>
                          <button type="button" class="btn btn-primary" @click="profileUpload">저장</button>
                        </div>
                      </div>
                    </div>
                  </div>

                </div>
                <div class="ms-3" style="margin-top: 130px;">
                  <h4 class="text-start">{{user?.username}}</h4>
                  <p>{{user?.email}}</p>
                </div>
              </div>
              <div class="p-4 text-black" style="background-color: #f8f9fa;">
                <div class="d-flex justify-content-end text-center py-1">
                  <div>
                    <p class="mb-1 h5">253</p>
                    <p class="small text-muted mb-0">Photos</p>
                  </div>
                  <div class="px-3" @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{user?.followers_cnt}}</p>
                    <p class="small text-muted mb-0">Followers</p>
                  </div>
                  <div @click="goToFriendList" style="cursor: pointer;">
                    <p class="mb-1 h5">{{user?.followings_cnt}}</p>
                    <p class="small text-muted mb-0">Following</p>
                  </div>
                </div>
              </div>
              <div class="card-body p-4 text-black">
                <div class="mb-5">
                  <p class="lead fw-normal mb-1">About</p>
                  <div class="p-4" style="background-color: #f8f9fa;">
                    <p class="font-italic mb-1">Web Developer</p>
                    <p class="font-italic mb-1">Lives in New York</p>
                    <p class="font-italic mb-0">Photographer</p>
                  </div>
                </div>
                <div class="d-flex justify-content-between align-items-center mb-4">
                  <p class="lead fw-normal mb-0">Recent photos</p>
                  <p class="mb-0"><a href="#!" class="text-muted">Show all</a></p>
                </div>
                <div class="row g-2">
                  <div class="col mb-2">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(112).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col mb-2">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(107).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
                <div class="row g-2">
                  <div class="col">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(108).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                  <div class="col">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(114).webp"
                      alt="image 1" class="w-100 rounded-3">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp"
          alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
          style="width: 150px; z-index: 1">
    </section>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import bootstrap from 'bootstrap/dist/js/bootstrap.js';

export default {
  name: 'MyPageView',
  data() {
    return {
      uploadImg: null,
      uploadImgUrl: null,
      editProfileModal: null, 
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    openModal() {
      // Open the edit profile modal
      this.editProfileModal = new bootstrap.Modal(document.getElementById('editProfileModal'));
      this.editProfileModal.show();
    },

    handleFileChange(event) {
      const file = event.target.files[0];
      this.uploadImg = file;

      // FileReader 객체를 사용하여 이미지 파일을 읽고 데이터 URL로 변환
      const reader = new FileReader();
      reader.onload = (e) => {
        this.uploadImgUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    },    
    closeEditProfileModal() {
      if (this.editProfileModal) {
        this.editProfileModal.hide();
      }
    },
    profileUpload() {
      axios({
        method: 'put',
        url: `${API_URL}/accounts/update/`,
        data: { username: this.user.username, followings: this.user.followings, profile: this.uploadImg },
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
          'Content-Type': 'multipart/form-data'
        }
      })
      .then((res) => {
        console.log(res)
        this.editProfileModal.hide();

        this.$store.dispatch('getuser')
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getImageSrc(base64String) {
      return `data:image/png;base64, ${base64String}`; // Base64 데이터를 이미지 src 형식으로 변환
    },

    goToFriendList(){
      console.log(this.user.id)
      this.$router.push({name : 'friendslist', params:{id: this.user.id}})
    }
  }
}
</script>

<style>
</style>