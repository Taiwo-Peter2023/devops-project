resource "aws_ecs_cluster" "main" {
  name = "devops-cluster"
}

resource "aws_cloudwatch_log_group" "ecs_logs" {
  name = "/ecs/devops-app"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "devops-app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name      = "devops-app"
      image     = "taiwopeterolatunji/devops-app:latest"
      essential = true

      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = "/ecs/devops-app"
          awslogs-region        = "us-east-1"
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}


resource "aws_ecs_service" "app_service" {
  name            = "devops-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  load_balancer {
  target_group_arn = aws_lb_target_group.app_tg.arn
  container_name   = "devops-app"
  container_port   = 5000
}

  network_configuration {
    subnets = [
      aws_subnet.public_1.id,
      aws_subnet.public_2.id
    ]

    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }
}


