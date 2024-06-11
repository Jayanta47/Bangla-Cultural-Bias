from data_handler import *
from prompt_creator import *
from chatgpt import *
from datetime import datetime
from tqdm import tqdm
from response_processor import *

logger = logging.getLogger(__name__)
# To add the variables from .env file
#  export $(cat .env | xargs) && env


def generate_inference_data(
    data_handler: DataHandlerBase,
    prompt_creator: PromptCreator,
    model: Model,
    response_processor: ResponseProcessor,
    total: int = -1,
    calcualate_cost: bool = False,
):
    datapoints = data_handler.return_data_point(total)
    total_input_tokens = 0
    total_output_tokens = 0
    current_input_tokens = 0
    current_output_tokens = 0
    for data_point in tqdm(datapoints):
        current_index = data_point["ID"]
        logger.info(f"Current index: {current_index}")

        try:
            for iteration in range(2):
                logger.info("Iteration: " + str(iteration))
                if iteration == 0:
                    prompt = prompt_creator.create_prompt(
                        prompt=data_point["text"],
                    )
                else:
                    prompt = prompt_creator.refine_prompt(
                        prompt_list=prompt,
                        response=response,
                    )

                model_response = model.create_response(prompt)
                response = model_response["content"]
                (status, modified_response) = response_processor.process_response(
                    response
                )

                if calcualate_cost:
                    current_input_tokens = model_response["input_tokens"]
                    current_output_tokens = model_response["output_tokens"]
                if status == 1:
                    break
        except Exception as e:
            logger.error(f"Error in creating response for index {current_index}")
            logger.error(e)
            continue

        if status == 0:
            logger.error(f"INCORRECT RESPONSE FOR {current_index}: {modified_response}")
        data_handler.save_generated_data(modified_response, index=current_index)

        if calcualate_cost:
            total_input_tokens += current_input_tokens
            total_output_tokens += current_output_tokens
            cost = model.calculate_cost(current_input_tokens, current_output_tokens)
            cost_till_now = model.calculate_cost(
                total_input_tokens, total_output_tokens
            )
            logger.info(
                f"Cost for index {current_index}: {cost}, Total cost: {cost_till_now}"
            )

            current_input_tokens = 0
            current_output_tokens = 0


def sanitize_log_name(filename):
    return filename.replace(" ", "_").replace(":", "_").replace("-", "_")


if __name__ == "__main__":
    logging.basicConfig(
        filename=sanitize_log_name(f"./logs/data_generation_{datetime.now()}.log"),
        level=logging.INFO,
    )
    # with open("hf_token.txt", "r") as f:
    #     token = f.read().strip("\n")
    data_handler = DataHandler("config.yaml")
    message_creator = ChatGptMessageCreator()
    response_processor = ResponseProcessor()
    logger.info(f"Model name: {data_handler.get_model_name()}")
    model = ChatgptModel(model_name=data_handler.get_model_name())
    logger.info("Data generation started")
    generate_inference_data(
        data_handler=data_handler,
        prompt_creator=message_creator,
        model=model,
        response_processor=response_processor,
        total=-1,
        calcualate_cost=True,
    )

    logger.info("Data generation finished")
