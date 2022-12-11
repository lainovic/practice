function loginUser(email, password) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("[LOG] We got the user data for:", email);
      resolve({ email, token: "32dsafdsfvcxve6GEXYZ" });
    }, 1000);
  });
}

function getUserVideos({ token }) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("[LOG] We got the user videos for:", token);
      resolve({
        [token]: ["video1", "video2", "video3"],
      });
    }, 1000);
  });
}

function getVideoDetails(video) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log("[LOG] We got the video details for:", video);
      resolve({
        [video]: {
          codec: "x265",
          bitrateInMbps: 4,
        },
      });
    }, 1000);
  });
}

function useDetails(details) {
  return new Promise((resolve, reject) => {
    console.log("[LOG] Error while parsing", details);
    reject(new Error("Internal error."));
  });
}

// loginUser("foo@bar.com", "hunter2")
//   .then((user) => {
//     console.log("-->", user);
//     return getUserVideos(user);
//   })
//   .then((videos) => {
//     console.log("-->", videos);
//     return getVideoDetails(videos[Object.keys(videos)[0]][0]);
//   })
//   .then((details) => {
//     console.log("-->", details);
//     return useDetails(details[Object.keys(details)[0]]);
//   })
//   .catch((err) => {
//     console.error("-->", err.message);
//   });

async function run() {
  try {
    const user = await loginUser("foo@bar.com", "hunter2");
    console.log("-->", user);
    const videos = await getUserVideos(user);
    console.log("-->", videos);
    const details = await getVideoDetails(videos[Object.keys(videos)[0]][0]);
    console.log("-->", details);
    const _ = await useDetails(details[Object.keys(details)[0]]);
  } catch (error) {
    console.error("-->", error.message);
  }
}

console.log("start");
run();
console.log("end");
