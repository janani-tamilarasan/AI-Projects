import { useState } from "react";
import { uploadResume } from "../services/resumeService";

export default function ResumeUpload() {

    const [file, setFile] = useState();

    const [jobDescription, setJobDescription] = useState("");

    const [loading, setLoading] = useState(false);

    const [result,setResult] = useState(null);
    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const response = await uploadResume(
                file,
                jobDescription
            );

            setResult(response);;

        } catch (err) {

            console.log

            alert("Upload Failed");

            console.log(err);

        }

        setLoading(false);

    };

    return (

        <form onSubmit={handleSubmit}>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <br />
            <label> Job Description</label>
            <textarea
                rows="10"
                value={jobDescription}
                onChange={(e)=>
                    setJobDescription(
                        e.target.value
                    )
                }
            />

            <br />

            <button>

                Upload Resume

            </button>

            <br/>

            {loading && <p>Analyzing...</p>}

            {
            result && (

            <div>

                <h2>
                    Match Score: {result.match_score}%
                </h2>


                <hr />


                <h3>
                    Matched Skills
                </h3>

                <ul>
                    {
                    result.matched_skills?.map(
                        (skill,index)=>(

                            <li key={index}>
                                {skill}
                            </li>

                        )
                    )
                    }
                </ul>


                <h3>
                    Missing Skills
                </h3>

                {
                    result.missing_skills?.length === 0 ?

                    <p>
                        🎉 No missing skills
                    </p>

                    :

                    <ul>
                        {
                        result.missing_skills.map(
                            (skill,index)=>(

                                <li key={index}>
                                    {skill}
                                </li>

                            )
                        )
                        }
                    </ul>
                }


                <h3>
                    Experience Summary
                </h3>

                <p>
                    {result.experience_summary}
                </p>


                <h3>
                    Recommendation
                </h3>

                <p>
                    {result.recommendation}
                </p>


            </div>

            )
            }

        </form>

    );

}