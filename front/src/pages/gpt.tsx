import { useForm } from "react-hook-form";
import { useGpt } from "../hooks/useGpt";
import Output from "../components/gptOut";
// 채팅 메시지 목록을 상태로 관리
import { useState, useEffect } from "react";
import OutputError from "../components/gptError";
import { rest } from "lodash";
const Gpt = () => {
    const { register, handleSubmit, watch, reset } = useForm();

    // inputData의 현재 값을 watch로 감시
    const inputValue = watch("inputData", "");
    // inputValue가 비어있으면 버튼을 비활성화하기 위한 변수
    const isButtonDisabled = !inputValue || inputValue.trim() === "";

    type ChatMessage = {
        role: "user" | "gpt";
        content: string | null;
    };

    const [messages, setMessages] = useState<ChatMessage[]>([
        { role: "gpt", content: "안녕하세요! 무엇을 도와드릴까요?" },
    ]);

    // 사용자가 메시지를 보낼 때 messages에 추가
    const onSubmit = (input: string) => {
        reset({ inputData: "" });
        setMessages((prev) => [...prev, { role: "user", content: input }]);
        mutate(input, {
            onSuccess: (response) => {
                setMessages((prev) => [
                    ...prev,
                    { role: "gpt", content: response },
                ]);
            },
            onError: () => {
                setMessages((prev) => [
                    ...prev,
                    { role: "gpt", content: "에러입니다" },
                ]);
            },
        });
        
        console.log("폼 데이터:", input);
    };

    const { mutate } = useGpt();

    return (
        <main className="main-wrap">
            <section
                className="gpt-chat-container"
                style={{
                    maxWidth: 600,
                    margin: "0 auto",
                    padding: 24,
                    background: "#f5f5f7",
                    borderRadius: 12,
                    maxHeight: 700,
                    minHeight: 500,
                    display: "flex",
                    flexDirection: "column",
                    overflowY: "auto",
                }}
            >
                <div style={{ flex: 1, overflowY: "auto", marginBottom: 16 }}>
                    {/* 예시 메시지 */}
                    {/* 이미 위에서 setMessages를 통해 메시지를 이어 붙이는(onSubmit, useEffect) 로직을 구현했으므로,
            여기서는 messages 배열을 map으로 렌더링만 하면 됩니다. */}
                    <div
                        style={{
                            display: "flex",
                            flexDirection: "column",
                            gap: 12,
                        }}
                    >
                        {messages.map((msg, idx) =>
                            msg.role === "user" ? (
                                <div
                                    key={idx}
                                    style={{
                                        alignSelf: "flex-end",
                                        background: "#007aff",
                                        color: "#fff",
                                        padding: "10px 16px",
                                        borderRadius: 16,
                                        maxWidth: "80%",
                                    }}
                                >
                                    {msg.content}
                                </div>
                            ) : (
                                msg.content && (
                                    <Output key={idx} result={msg.content} />
                                )
                            )
                        )}
                        {/* {isError && <OutputError />} */}
                    </div>
                </div>
                <form
                    style={{ display: "flex", gap: 8 }}
                    onSubmit={handleSubmit((data) => onSubmit(data.inputData))}
                >
                    <input
                        type="text"
                        {...register("inputData")}
                        placeholder="메시지를 입력하세요..."
                        style={{
                            flex: 1,
                            padding: "10px 16px",
                            borderRadius: 16,
                            border: "1px solid #ccc",
                            outline: "none",
                            fontSize: 16,
                            background: "#fff",
                        }}
                    />
                    <button
                        type="submit"
                        style={{
                            background: "#007aff",
                            color: "#fff",
                            border: "none",
                            borderRadius: 16,
                            padding: "0 20px",
                            fontSize: 16,

                            // cursor: "not-allowed"
                        }}
                        disabled={isButtonDisabled}
                    >
                        전송
                    </button>
                </form>
                <div
                    style={{
                        fontSize: 12,
                        color: "#888",
                        marginTop: 8,
                        textAlign: "center",
                    }}
                >
                    (데모 화면입니다. 실제로 메시지를 보낼 수 없습니다.)
                </div>
            </section>
        </main>
    );
};
export default Gpt;
