import api from "../api/api";


export async function uploadResume(
    file,
    jobDescription
){

    const formData = new FormData();


    formData.append(
        "file",
        file
    );


    formData.append(
        "job_description",
        jobDescription
    );


    const response = await api.post(
        "/resume/upload",
        formData,
        {
            headers:{
                "Content-Type":
                "multipart/form-data"
            }
        }
    );


    return response.data;

}