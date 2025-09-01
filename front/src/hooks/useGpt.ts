import { useMutation } from "@tanstack/react-query";
import { goGpt } from "../api/gptAPI";

export const useGpt = () => {
    return useMutation({
        mutationFn: goGpt
    })
}