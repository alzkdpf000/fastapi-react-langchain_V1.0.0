

export const goGpt = async (query: string) => {
    const response = await fetch(`http://localhost:8000/home?query=${query}`);
    // const response = await fetch(`http://localhost:8000/`);
    const data = await response.json();
    console.log(data);

    if (!response.ok) {
        const error = await response.text();
        throw new Error(error || "오류가 나왔어요");
    }
    return data.response;
}