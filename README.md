# PaliGemma-2 Tools

This is a collection of tools for exploring what can be done with PaliGemma-2 for
object detection.

## Tools

1. `detect_cli.py` - Apply PaliGemma-2 to an image.
1. `apply_paligemma2.py` - Apply PaliGemma-2 to a video.


## To Do

1. Set up caching of models that is permanent across container
   restarts:
   * [https://www.google.com/search?client=firefox-b-d&q=hugging+face+download+and+cache+paligemma2+model+instead+of+calling++PaliGemmaForConditionalGeneration.from_pretrained%28%29+each+time](https://www.google.com/search?client=firefox-b-d&q=hugging+face+download+and+cache+paligemma2+model+instead+of+calling++PaliGemmaForConditionalGeneration.from_pretrained%28%29+each+time)
   * [https://www.google.com/search?client=firefox-b-d&q=hugging+face+global+cache+path](https://www.google.com/search?client=firefox-b-d&q=hugging+face+global+cache+path)
   * [https://huggingface.co/docs/huggingface_hub/guides/manage-cache](https://huggingface.co/docs/huggingface_hub/guides/manage-cache)
   * [https://huggingface.co/docs/hub/local-cache](https://huggingface.co/docs/hub/local-cache)
2. Batching when processing video
3. Write up notes on prompt selection from gemini
4. What sort of video was SigLIP trained on? What was mix trained on
   for detection
5. Get video associated with above - it will help sort out if problem is in image or text encoder


## References

* [https://ai.google.dev/gemma/docs/paligemma](https://ai.google.dev/gemma/docs/paligemma)
* [https://huggingface.co/blog/paligemma](https://huggingface.co/blog/paligemma)
* [https://blog.roboflow.com/fine-tune-paligemma-2/](https://blog.roboflow.com/fine-tune-paligemma-2/)
* [https://huggingface.co/blog/paligemma2](https://huggingface.co/blog/paligemma2)
* [https://huggingface.co/docs/transformers/en/model_doc/paligemma](https://huggingface.co/docs/transformers/en/model_doc/paligemma)
* [https://ai.google.dev/gemma/docs/paligemma/prompt-system-instructions](https://ai.google.dev/gemma/docs/paligemma/prompt-system-instructions)
