export const uploadImageToImgBB = async ({ image, name }) => {
  try {
    const peticion = await fetch(
      `https://api.imgbb.com/1/upload?key=${process.env.KEY_IMGBB}&name=${name}&image=${image}`,
      {
        headers: { Accept: "application/json" },
        method: "POST",
        body: JSON.stringify({}),
      }
    );
    const result = await peticion;
    console.log(result, "image uploaded successfully");
  } catch (error) {
    console.error(error, "error uploading image");
  }
};
